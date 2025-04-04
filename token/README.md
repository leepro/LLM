# Tokenizer

* [TikToken](https://github.com/openai/tiktoken)
* [Web TikToken](https://tiktokenizer.vercel.app/)

![TikToken](https://raw.githubusercontent.com/leepro/LLM/main/assets/tiktoken.png)

## GPT2

```
% python3 ./tik_token.py
token ids= [16, 362, 513, 7795, 15231, 4751, 31619, 224, 246, 167, 232, 242, 220, 47991, 250, 166, 113, 255, 35975, 116, 23821, 252, 227, 46695, 230, 46695, 97, 13, 314, 716, 257, 2933, 13]
[00] =>         [16] =>         [1]
[01] =>         [362] =>        [ 2]
[02] =>         [513] =>        [ 3]
[03] =>         [7795] =>       [ 1998]
[04] =>         [15231] =>      [ 1975]
[05] =>         [4751] =>       [ 2000]
[06] =>         [31619] =>      [ �]
[07] =>         [224] =>        [�]
[08] =>         [246] =>        [�]
[09] =>         [167] =>        [�]
[10] =>         [232] =>        [�]
[11] =>         [242] =>        [�]
[12] =>         [220] =>        [ ]
[13] =>         [47991] =>      [�]
[14] =>         [250] =>        [�]
[15] =>         [166] =>        [�]
[16] =>         [113] =>        [�]
[17] =>         [255] =>        [�]
[18] =>         [35975] =>      [�]
[19] =>         [116] =>        [�]
[20] =>         [23821] =>      [ �]
[21] =>         [252] =>        [�]
[22] =>         [227] =>        [�]
[23] =>         [46695] =>      [�]
[24] =>         [230] =>        [�]
[25] =>         [46695] =>      [�]
[26] =>         [97] =>         [�]
[27] =>         [13] =>         [.]
[28] =>         [314] =>        [ I]
[29] =>         [716] =>        [ am]
[30] =>         [257] =>        [ a]
[31] =>         [2933] =>       [ boy]
[32] =>         [13] =>         [.]
```

## GPT-4o

```
token ids= [16, 220, 17, 220, 18, 220, 3204, 23, 220, 5695, 20, 220, 1179, 15, 112252, 52971, 5544, 119833, 13, 357, 939, 261, 8473, 13]
[00] =>         [16] =>         [1]
[01] =>         [220] =>        [ ]
[02] =>         [17] =>         [2]
[03] =>         [220] =>        [ ]
[04] =>         [18] =>         [3]
[05] =>         [220] =>        [ ]
[06] =>         [3204] =>       [199]
[07] =>         [23] =>         [8]
[08] =>         [220] =>        [ ]
[09] =>         [5695] =>       [197]
[10] =>         [20] =>         [5]
[11] =>         [220] =>        [ ]
[12] =>         [1179] =>       [200]
[13] =>         [15] =>         [0]
[14] =>         [112252] =>     [ 나는]
[15] =>         [52971] =>      [ 한국]
[16] =>         [5544] =>       [인]
[17] =>         [119833] =>     [ 입니다]
[18] =>         [13] =>         [.]
[19] =>         [357] =>        [ I]
[20] =>         [939] =>        [ am]
[21] =>         [261] =>        [ a]
[22] =>         [8473] =>       [ boy]
[23] =>         [13] =>         [.]
```
