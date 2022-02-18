import torchtext.legacy.data as data
import torch.nn as nn
import os
dir=os.path.dirname(os.path.realpath(__file__))

eng = data.Field()
translation_STE = data.Field()

fields = {"quote":('q',eng),"translation":('tr',translation_STE)}

train = data.TabularDataset(path=dir+'/data/file.txt',format='json',fields=fields)

eng.build_vocab(train)
translation_STE.build_vocab(train)

train_iter = data.BucketIterator(dataset=train, batch_size=60,shuffle=False)
train_batch = next(iter(train_iter))
_iter=7
first_q = list(map(lambda x: eng.vocab.itos[x],train_batch.q[:,_iter]))
print(first_q)
first_tr = list(map(lambda x: translation_STE.vocab.itos[x],train_batch.tr[:,_iter]))
print(first_tr)

class Encoder(nn.Module):
	pass
class Decoder(nn.Module):
	pass

