# Tacotron

## DataFeeder 
- batch별 max tokens로 padding=0 ('_')로 채워넣음
- data
| tokens (encoder input) 
| linear spectrum
| mel spectrum



## Encoder

- Char-Embedding -> Prenet -> CBHG(1-D convolution bank + highway network + bidirectional GRU)
	- prenet | 2layer denn
		1. ``char_embedded_inputs = \
	tf.nn.embedding_lookup(char_embed_table, inputs)`` 에서 해당 tokens id에 해당하는 초기화된 벡터 load 
	output shape =(, , 128)
	- CBHG |  1-Dconv -> max-pooling ->  two projection layers ->  highwaynet -> GRU
		1. filter size가 1~16까지의 convoultion결과물을 concat후 max-pooling
		2. highwaynet -> 네트워크의 깊이를 깊이하고 최적화하기 위한 network-
- Encoder output shape =(, ,128)

## Decoder

Prenet -> RNN -> CBHG
loss : mel-target + linear_target ( char-embedding부터 모든 weight update)
