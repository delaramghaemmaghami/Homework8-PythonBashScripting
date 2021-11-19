my_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]  # 17
print(sum(list(map(lambda word: word.lower().count("a"), my_list))))
