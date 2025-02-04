from django.conf import settings


class ChatService:
    """Singleton interface providing Chat channel manipulation methods.

    This abstraction is meant to be used by `models.ChatRoom`, not directly by
    developers. Implementations of this interface must be registered in Django
    settings under a dict named `CHAT_SERVICES` (see `models.ChatRoom` for
    details).
    """

    __instances = {}

    def __init__(self, settings):
        """Constructs the ChatService using a Django settings object.

        ChatService implementations must override this constructor.
        """
        raise NotImplementedError("Can't instantiate abstract ChatService class")

    @classmethod
    def get_instance(cls):
        if cls not in cls.__instances:
            cls.__instances[cls] = cls(settings)
        return cls.__instances[cls]

    def create_text_channel(self, guild_id, name, *args, **kwargs):
        raise NotImplementedError

    def get_text_channel_participants(self, channel_id):
        raise NotImplementedError

    def delete_text_channel(self, guild_id, channel_id):
        raise NotImplementedError

    def create_audio_channel(self, guild_id, name, *args, **kwargs):
        raise NotImplementedError

    def delete_audio_channel(self, guild_id, channel_id):
        raise NotImplementedError

    def create_channel_url(self, guild_id, channel_id, is_audio=False):
        raise NotImplementedError

    def categorize_channel(self, guild_id, channel_id, category_name):
        raise NotImplementedError

    def archive_channel(self, guild_id, channel_id, *args, **kwargs):
        raise NotImplementedError

    def unarchive_text_channel(self, guild_id, channel_id, *args, **kwargs):
        raise NotImplementedError

    def unarchive_voice_channel(self, guild_id, channel_id, *args, **kwargs):
        raise NotImplementedError

    def send_message(self, channel_id, msg, embedded_urls={}):
        raise NotImplementedError

    def announce(self, channel_id, msg, embedded_urls={}):
        raise NotImplementedError

    def handle_tag_added(self, channel_id, puzzle, tag_name):
        raise NotImplementedError

    def handle_tag_removed(self, channel_id, puzzle, tag_name):
        raise NotImplementedError

    def handle_puzzle_rename(self, channel_id, new_name):
        raise NotImplementedError
