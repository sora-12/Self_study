# Tacotron

## DataFeeder 
- batch별 max tokens로 padding=0 ('_')로 채워넣음
- data
| tokens (encoder input) 
| linear spectrum
| mel spectrum



## Encoder

Char-Embedding -> Prenet -> CBHG
prenet | 2layer denn
CBHG |  1-Dconv -> max-pooling ->  two projection layers ->  highwaynet 





## Decoder

Prenet -> RNN -> CBHG
loss : mel-target + linear_target ( char-embedding부터 모든 weight update)
