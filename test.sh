context=$1
testdata=$2
save_tokenized=$3
src_dict=$4
trg_dict=$5
model_dir=$6
model=$7
result_dir=$8

gpu_id=$9


export CUDA_VISIBLE_DEVICES="${gpu_id}"
export FAIRSEQPY=./fairseq-context/
source activate pytorch
python -m source.testing.prepare_test_data "${save_tokenized}" "${testdata}" "${context}"

bash source/testing/get_testing_data.sh process "${src_dict}" "${trg_dict}" "${save_tokenized}" "${save_tokenized}"


output_dir="${result_dir}"/"${model}"
model_path="${model_dir}""${model}"
target="${save_tokenized}"/bin
input_file="${save_tokenized}"/test.src
beam=1000


mkdir -p $output_dir


if [ "${context}" == "nocontext" ]; then
python "${FAIRSEQPY}"/generate.py -s src -t trg --path "${model_path}" --beam $beam  --nbest "${beam}" "${target}" --batch-size 1 < "${input_file}" > "${output_dir}"/output.tok.nbest.txt

else
  if [ "${gpu_id}" == "-1" ]; then
          python "${FAIRSEQPY}"/generate.py -s src -t trg --use-context --path "${model_path}" --beam $beam --nbest "${beam}" "${target}" --batch-size 16 < "${input_file}" > "${output_dir}"/output.tok.nbest.txt
  else
          python "${FAIRSEQPY}"/generate.py -s src -t trg --use-context --path "${model_path}" --beam $beam --nbest "${beam}" "${target}" --batch-size 1 < "${input_file}" > "${output_dir}"/output.tok.nbest.txt
  fi
fi
