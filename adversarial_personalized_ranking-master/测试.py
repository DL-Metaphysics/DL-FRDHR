parser.add_argument('--path', nargs='?', default='Data/', #输入数据路径
                        help='Input data path.')
    parser.add_argument('--dataset', nargs='?', default='yelp', #选择一个数据集
                        help='Choose a dataset.')
    parser.add_argument('--verbose', type=int, default=1,  #多少轮迭代输出一次
                        help='Evaluate per X epochs.')
    parser.add_argument('--batch_size', type=int, default=512,
                        help='batch_size')
    parser.add_argument('--epochs', type=int, default=2000,     #APR迭代总次数
                        help='Number of epochs.')
    parser.add_argument('--embed_size', type=int, default=64,   #MF分解出来的物品矩阵和用户矩阵的列数
                        help='Embedding size.')
    parser.add_argument('--dns', type=int, default=1,  #
                        help='number of negative sample for each positive in dns.')
    parser.add_argument('--reg', type=float, default=0,  #MF优化未加噪音构成的损失函数时用的正则化
                        help='Regularization for user and item embeddings.')
    parser.add_argument('--lr', type=float, default=0.05,   #学习率
                        help='Learning rate.')
    parser.add_argument('--reg_adv', type=float, default=1,   #MF优化加了噪音构成的损失函数时用的正则化
                        help='Regularization for adversarial loss')
    parser.add_argument('--restore', type=str, default=None,
                        help='The restore time_stamp for weights in \Pretrain')
    parser.add_argument('--ckpt', type=int, default=100,   #多少轮迭代保存一次
                        help='Save the model per X epochs.')
    parser.add_argument('--task', nargs='?', default='',  #对当前的任务命名
                        help='Add the task name for launching experiments')
    parser.add_argument('--adv_epoch', type=int, default=0,    #BPR迭代次数
                        help='Add APR in epoch X, when adv_epoch is 0, it\'s equivalent to pure AMF.\n '
                             'And when adv_epoch is larger than epochs, it\'s equivalent to pure MF model. ')
    parser.add_argument('--adv', nargs='?', default='grad',  #生成对抗样本的方法：梯度下降法或随机法 （详细转220行）
                        help='Generate the adversarial sample by gradient method or random method')
    parser.add_argument('--eps', type=float, default=0.5,  #l2范化的最小值边界
                        help='Epsilon for adversarial weights.')
    return parser.parse_args()
