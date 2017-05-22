class config():
    # env config
    render_train     = False
    render_test      = False
    overwrite_render = True
    record           = False
    high             = 255.

    # output config
    output_path  = "learning/results/q_learning/linear/"
    model_output = output_path + "model.weights/"
    log_path     = output_path + "log.txt"
    plot_output  = output_path + "scores.png"

    # model and training config
    n_hidden_layers   = 10
    num_episodes_test = 20
    grad_clip         = True
    clip_val          = 100
    saving_freq       = 5000
    log_freq          = 50
    eval_freq         = 1000
    soft_epsilon      = 0

    # hyper params
    nsteps_train       = 50000
    batch_size         = 64
    buffer_size        = 1000
    target_update_freq = 500
    gamma              = 0.99
    learning_freq      = 4
    state_history      = 5
    lr_begin           = 0.05
    lr_end             = 0.01
    lr_nsteps          = nsteps_train/2
    eps_begin          = 0.1
    eps_end            = 0.01
    eps_nsteps         = nsteps_train/2
    learning_start     = 200
