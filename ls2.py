# 1. Tính trung bình, trung vị và mode của một danh sách điểm số.
score = [5, 5, 8, 6, 9]
# mean_score = sum(score) / len(score) 
# print("Điểm trung bình là:", mean_score)
# median_score = sorted(score)[len(score) // 2]
# print("Điểm trung vị là:", median_score)
# mode_score = max(set(score), key=score.count) # Tìm giá trị xuất hiện nhiều nhất trong danh sách score
# print("Điểm mode là:", mode_score)
new_score = [float(input("Nhập điểm số mới: "))]
if new_score[0] < 0 or new_score[0] > 10:
    print("Điểm số không hợp lệ. Vui lòng nhập điểm số từ 0 đến 10.")
else:
    score.append(new_score[0]) # Thêm điểm số mới vào danh sách score
    print("Danh sách điểm số sau khi thêm điểm mới:", score)