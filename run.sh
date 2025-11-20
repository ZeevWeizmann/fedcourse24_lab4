
echo "=> Generate data.."

cd data/ 

rm -r mnist/all_data

python generate_data.py \
  --dataset mnist \
  --n_clients 10 \
  --non_iid \
  --frac 0.1 \
  --save_dir mnist \
  --seed 1234


