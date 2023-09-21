from fold_evaluator import FoldEvaluator

if __name__ == "__main__":
    inputs = ["bands",
              "R20m_bands",
              "R20m_R10m_bands",
              "R20m_R60m_bands",
              "props_ex_som",
              "all_ex_som"
              ]

    configs = []
    for i in inputs:
        configs.append({"input": i})
    c = FoldEvaluator(configs=configs, prefix="t2", folds=10, algorithms=["mlr","svr","ann"])
    c.process()