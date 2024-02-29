def truth_table():
    # 表頭
    print("P\tQ\tP∧Q\tP∨Q\tP→Q\tP←Q\tP↔Q")

    # 遍歷所有可能的P和Q的取值
    for p in [True, False]:
        for q in [True, False]:
            # AND
            result_and = p and q
            # OR
            result_or = p or q
            # IF-THEN
            result_if_then = (not p) or q
            # WHEN
            result_when = (not p) or (p and q)
            # IF-AND-ONLY-IF
            result_iff = (p == q)

            # 輸出結果
            print(f"{p}\t{q}\t{result_and}\t{result_or}\t{result_if_then}\t{result_when}\t{result_iff}")

# 執行函數
truth_table()

