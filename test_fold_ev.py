from fold_evaluator import FoldEvaluator

if __name__ == "__main__":
    inputs = ["bands",
              "props_ex_som",
              "all_ex_som"
              ]

    configs = []
    for i in inputs:
        configs.append({"input": i})
    c = FoldEvaluator(configs=configs, prefix="all", folds=10, algorithms=["mlr","svr","ann"])
    c.process()