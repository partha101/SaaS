def sum_2_n(list,n)
	flag=0
	for i in 0...list.length
		for j in 0...list.length
			if list[i]+list[j]==n
			flag=1
			end
		end
		if flag==1
			puts true.to_s
			break
		end
	end


