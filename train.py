#
#
import torch
import model
import dataset


#
#
m = model.Bert()


#
#
opt = torch.optim.Adam(m.parameters(), lr=0.01)


#
#
ds = [dataset.generate_item_pattern() for _ in range(5)]


#
#
trn_ds = ds[:4]
tst_ds = ds[4:]
print(trn_ds)
print(tst_ds)


#
#
for _ in range(10):
  for ptrn, trgt in trn_ds:
    opt.zero_grad()
    inpt = [dataset.tkn2idx[tkn] for tkn in ptrn]
    tIdx = dataset.tkn2idx[trgt]
    qIdx = ptrn.index('?')
    print(ptrn, inpt)
    print(trgt, tIdx)
    mOut = m(torch.tensor(inpt))
    print(mOut)
    pQst = mOut[qIdx]
    print(pQst)
    pTgt = pQst[tIdx]
    print(pTgt)
    loss = -torch.log(pTgt)
    print('TRN:', loss)
    loss.backward()
    opt.step()

  for cIdx, (ptrn, trgt) in enumerate(tst_ds):
    inpt = [dataset.tkn2idx[tkn] for tkn in ptrn]
    tIdx = dataset.tkn2idx[trgt]
    qIdx = ptrn.index('?')
    mOut = m(torch.tensor(inpt))
    pQst = mOut[qIdx]
    pTgt = pQst[tIdx]
    loss = -torch.log(pTgt)
    print('TST:', cIdx, loss)
