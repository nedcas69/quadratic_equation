puts "Введите значение а"
s = STDIN.gets.chomp
puts "Введите значение b"
n = STDIN.gets.chomp
puts "Введите значение c"
v = STDIN.gets.chomp
a = s.scan(/\d/).join('')
b = n.scan(/\d/).join('')
c = v.scan(/\d/).join('')
if a != '' && b != '' && c != ''
a = a.to_f
b = b.to_f
c = c.to_f
    if a != 0
        discr = b*b - 4*a*c
        if discr > 0
            x1 = (-b-discr**0.5)/(a*2)
            x2 = (-b+discr**0.5)/(a*2)
            puts "x1 = #{x1.to_s}  "
            puts "x2 = #{x2.to_s}  "
        elsif discr == 0
            x = -b/(2*a)
            puts "x = #{x.to_s}"
        else
            puts "Нет корней!"
        end
    else
        if b != 0
            x = -c/b
            puts "x = #{x.to_s}" 
        else
            if c !=0
                puts 'Решений нет!'
            else
                puts "x любое значение!"
            end
        end

    end

else
    puts "#{s}x^2+#{n}x+#{v}=0 "
end