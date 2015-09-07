class BookItem
	def initialize(isbn,price)
		if isbn.length==0
			raise ArgumentError
		end
		@isbn=isbn
		@price=price.to_f
	end
	def price_as_string
		print "$"+@price.to_s
	end
end
puts "enter the isbn"
isbn=gets.chomp
puts "enter the price"
price=gets.chomp
defo=BookItem.new(isbn,price)
defo.price_as_string

		
