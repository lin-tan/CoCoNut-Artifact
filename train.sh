train_script=$1
gpu_id=$2
export FAIRSEQPY=./fairseq-context/
source activate pytorch
export CUDA_VISIBLE_DEVICES="${gpu_id}"
echo "Start training"
python -m source.training.autoscript."${train_script}"
echo "End training"
