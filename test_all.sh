dic_dir=./intermediate_repo/java/2006/nocontext/train/bin
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_1/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_2/ -1 &
#bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_3/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_4/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_5/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_6/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_7/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_8/ -1 &
#bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_9/ -1 &
# bash test.sh nocontext defects4j ./data/test/defects4j/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_fconv_tuned_10/ -1


dic_dir=./intermediate_repo/java/2006/context/train/bin
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_1/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_1/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_2/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_2/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_3/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_3/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_4/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_4/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_5/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_5/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_6/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_6/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_7/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_7/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_8/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_8/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_9/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_9/ -1 &
bash test.sh context quixbugs ./data/test/quixjava/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_10/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_context_tuned_10/ -1


dic_dir=./intermediate_repo/java/2006/context/train/bin
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_1/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_1/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_2/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_2/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_3/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_3/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_4/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_4/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_5/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_5/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_6/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_6/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_7/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_7/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_8/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_8/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_9/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_9/ -1 &
bash test.sh context defects4j ./data/test/defects4j/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/fixed_context_tuned_10/ checkpoint_best.pt ./intermediate_repo/java/2006/results/d4j_context_tuned_10/ -1


dic_dir=./intermediate_repo/java/2006/nocontext/train/bin
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_1/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_2/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_3/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_4/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_5/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_6/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_7/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_8/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_9/ -1 &
# bash test.sh nocontext quixbugs ./data/test/quixjava/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/java/2006/results/quixjava_fconv_tuned_10/ -1




#dic_dir=./intermediate_repo/js/nocontext/train/bin
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_1/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_2/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_3/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_4/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_5/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_6/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_7/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_8/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_9/ -1 &
#bash test.sh nocontext bugaid ./data/test/bugaid/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_fconv_tuned_10/ -1


##dic_dir=./intermediate_repo/js/context/train/bin
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_1/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_1/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_2/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_2/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_3/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_3/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_4/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_4/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_5/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_5/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_6/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_6/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_7/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_7/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_8/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_8/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_9/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_9/ -1
##bash test.sh context bugaid ./data/test/bugaid/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/js/context/trained/context_tuned_10/ checkpoint_best.pt ./intermediate_repo/js/results/bugaid_context_tuned_10/ -1
##'''

#dic_dir=./intermediate_repo/python/nocontext/train/bin
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_1/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_2/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_3/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_4/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_5/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_6/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_7/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_8/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_9/ -1 &
#bash test.sh nocontext quixpy ./data/test/quixpy/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_fconv_tuned_10/ -1


dic_dir=./intermediate_repo/python/context/train/bin
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_1/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_1/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_2/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_2/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_3/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_3/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_4/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_4/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_5/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_5/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_6/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_6/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_7/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_7/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_8/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_8/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_9/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_9/ -1 &
bash test.sh context quixpy ./data/test/quixpy/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/python/context/trained/context_tuned_10/ checkpoint_best.pt ./intermediate_repo/python/results/quixpy_context_tuned_10/ -1



#dic_dir=./intermediate_repo/c/nocontext/train/bin
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_1/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_2/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_3/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_4/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_5/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_6/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_7/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_8/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_9/ -1 &
#bash test.sh nocontext manybugs ./data/test/manybugs/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_fconv_tuned_10/ -1

##'''
##dic_dir=./intermediate_repo/c/context/train/bin
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_1/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_1/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_2/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_2/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_3/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_3/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_4/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_4/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_5/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_5/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_6/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_6/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_7/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_7/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_8/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_8/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_9/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_9/ -1 &
##bash test.sh context manybugs ./data/test/manybugs/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/context/trained/context_tuned_10/ checkpoint_best.pt ./intermediate_repo/c/results/manybugs_context_tuned_10/ -1
##'''

#dic_dir=./intermediate_repo/c/nocontext/train/bin
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_1/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_2/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_3/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_4/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_5/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_6/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_7/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_8/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_9/ -1 &
#bash test.sh nocontext codeflaws ./data/test/codeflaws/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/c/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/c/results/codeflaws_fconv_tuned_10/ -1


dic_dir=./intermediate_repo/java/2006/nocontext/train/bin
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_1/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_1/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_2/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_2/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_3/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_3/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_4/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_4/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_5/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_5/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_6/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_6/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_7/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_7/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_8/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_8/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_9/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_9/ -1 &
# bash test.sh nocontext codrep ./data/test/codrep/nocontext/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/nocontext/trained/fconv_tuned_10/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_fconv_tuned_10/ -1

##'''
##dic_dir=./intermediate_repo/java/2006/context/train/bin
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_1/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_1/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_2/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_2/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_3/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_3/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_4/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_4/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_5/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_5/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_6/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_6/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_7/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_7/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_8/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_8/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_9/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_9/ -1
##bash test.sh context codrep ./data/test/codrep/context/ ${dic_dir}/dict.src.txt ${dic_dir}/dict.trg.txt ./intermediate_repo/java/2006/context/trained/context_tuned_10/ checkpoint_best.pt ./intermediate_repo/java/2006/results/codrep_context_tuned_10/ -1
##'''

#lstm

#transformer

#variance