from rest_framework import serializers

from api.models import User, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'users'
        model = User
        fields = ('id', 'full_name', 'email', 'password')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'users'
        model = User
        fields = ('id', 'full_name', 'email')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'posts'
        model = Post
        fields = ('id', 'title', 'text', 'user')


class PostGetSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        db_table = 'posts'
        model = Post
        fields = ('id', 'title', 'text', 'user')


class CommentSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        db_table = 'comments'
        model = Comment
        fields = ('id', 'post', 'c_text', 'user')

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('user')
        return queryset


class PostDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()

    user = UserInfoSerializer()
    # comment = serializers.SerializerMethodField()
    comment = CommentSerializer(read_only=True, source="comment_set", many=True)




