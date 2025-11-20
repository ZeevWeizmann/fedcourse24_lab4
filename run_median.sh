for p in 0 0.1 0.3 0.5
do
    echo "=============================================="
    echo " Running MEDIAN experiment with prop=$p "
    echo "=============================================="

    SAFE_P=${p//./_}   
    LOGDIR="logs/mnist_median_prop_non_iid_${SAFE_P}"
    mkdir -p "$LOGDIR"

    python train.py \
        --experiment "mnist" \
        --n_rounds 25 \
        --local_steps 1 \
        --local_optimizer sgd \
        --local_lr 0.001 \
        --server_optimizer sgd \
        --server_lr 0.1 \
        --bz 128 \
        --device "cpu" \
        --log_freq 1 \
        --verbose 1 \
        --logs_dir "$LOGDIR" \
        --prop $p \
        --seed 12 \
        --n_clients 10 \
        --aggregator_type "median" \
        2>&1 | tee "$LOGDIR/output.txt"

done
