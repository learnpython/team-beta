from haystack import indexes
from contragents.models import Contragent


class ContragentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')
    region = indexes.CharField(model_attr='region')
    
    def get_model(self):
        return Contragent