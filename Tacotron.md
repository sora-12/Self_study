# Tacotron

## DataFeeder 
- batch별 max tokens로 padding=0 ('_')로 채워넣음
- data
| tokens (encoder input) 
| linear spectrum
| mel spectrum



## Encoder

- Char-Embedding -> Prenet -> CBHG  
	- prenet | 2layer denn
		1. ``char_embedded_inputs = \
	tf.nn.embedding_lookup(char_embed_table, inputs)`` 에서 해당 tokens id에 해당하는 초기화된 벡터 load 
	output shape =(, , 128)
	- CBHG |  1-Dconv -> max-pooling ->  two projection layers ->  highwaynet 
		1. filter size가 1~16까지의 convoultion결과물을 concat후 max-pooling
		2. highwaynet -> 네트워크의 깊이를 깊이하고 최적화하기 위한 network-
- Encoder output shape =(, ,128)

## Attention

## Decoder

- Prenet -> RNN -> CBHG 
- loss : mel-target + linear_target ( char-embedding부터 모든 weight update)
	- RNN
	1. attention이 적용된 cell과 RNN결합
	2. Reduction_factor만큼 생성된  Mel-Spectrogram은 PostNet에 해당하는 CBHG를 거치게 되며 최	 종적으로 Linear-Spectrogram을 생성하게 된다.
	```
	decoder_outputs, _), final_decoder_state, _ =  tf.contrib.seq2seq.dynamic_decode(
	BasicDecoder(output_cell, helper,decoder_init_state),maximum_iterations=hp.max_iters)
	```
	3. 
	

