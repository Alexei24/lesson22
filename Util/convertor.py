from model.human import Human
class Convertor:

    @staticmethod
    def convert_to_string(humans):
        s = "List of humans: \n"

        if not isinstance(humans, (list, tuple)):
            return "List is emty: "

        for human in humans:
            if isinstance(human, Human):
                s += "\n" + str(human)
        return s