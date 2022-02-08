from PyUtils.Obj2Json import Obj2Json


class TopicDialogs:

    def __init__(self):
        """Default TopicDialogs constructor"""
        # name of the topic
        self.topic_name = ""
        # Eg.: DSilHand_KylmirShadeSkinner
        self.actor_name = ""
        # Player prompt
        self.player_dialog = ""
        # Form ID
        self.form_id = ""
        # Tuples of NPC topic information
        self._list_topic_data = []

    def to_string(self):
        obj = Obj2Json()
        obj.add("topic_name", self.topic_name)
        obj.add("actor_name", self.actor_name)
        obj.add("player_dialog", self.player_dialog)
        obj.add("form_id", self.form_id)
        obj.addl("_list_topic_data", self._list_topic_data)
        return obj.obj()

    def add_topic_data(self, index: str, response: str, mood: str):
        """Add a tuple of topic information."""
        topic_tuple = [index, response, mood]
        self._list_topic_data.append(topic_tuple)

    def sort(self):
        """Sorts this topic information"""
        self._list_topic_data = sorted(self._list_topic_data, key=lambda tup: tup[0])

    def get_topic_data(self):
        """recover this topic information."""
        sorted_topic_list = sorted(self._list_topic_data, key=lambda tup: tup[0])
        self._list_topic_data = sorted_topic_list
        return sorted_topic_list

    def clear(self):
        """Clear _list_topic_data."""
        self._list_topic_data.clear()