puts "enter the number of terms to be entered"
x=gets.chomp.to_i
list1=[]
x.times do
	z=gets.chomp.to_i
	list1<<z
end
max=list1[0]
sum=0
list1.each do |x|
	if x>max
		max=x
	end
end
sum=sum+max
list1.delete(max)
max=list1[0]
list1.each do |x|
	if x>max
		max=x
	end
end 
sum=sum+max
print sum


		
	

