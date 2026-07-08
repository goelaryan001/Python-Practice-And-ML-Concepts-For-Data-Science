Select distinct l1.num as ConsecutiveNums
From Logs l1
Join Logs l2 on l1.id=l2.id-1 and l1.num=l2.num
Join Logs l3 on l2.id=l3.id-1 and l2.num=l3.num