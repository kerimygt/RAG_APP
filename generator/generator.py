class Generator:
    def generate(self, context):
        if isinstance(context, list):
            return " ".join([item['answer'] for item in context])
        return context['answer']
