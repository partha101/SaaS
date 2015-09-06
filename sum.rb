puts "enter the number of terms to be stored"
x=gets.chomp.to_i
list1=[]
x.times do
	z=gets.chomp.to_i
	list1<<z
end
	
sum=0
if list1.length==0
	return 0
else 
	list1.each {|x| sum=sum+x}
	print sum.to_s
end
