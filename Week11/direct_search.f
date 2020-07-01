        program direct_search
        implicit double precision(a-h,o-z)
        external func01_aosc658c

        xtol=1.E-2
        write(6,700)
700     format('Enter starting point for search interval : ',$)
        read(5,*)x_beg
        
        write(6,702)
702     format('Enter ending point for search interval   : ',$)
        read(5,*)x_end

        write(6,704)
704     format('Enter error tolerance for roots ',
     +          '(i.e., 1.E-2, 1.E-4) : ',$)        
        read(5,*)xtol

        number_int=nint((x_end-x_beg)/xtol)+1
        delta_x=(x_end-x_beg)/float(number_int)

        i_func_call=0
        i_root=0

        x_sub_beg=x_beg
        x_sub_end=x_sub_beg+delta_x

        do i_int=1,number_int
           i_func_call=i_func_call+1
           f_A=func01_aosc658c(x_sub_beg)
           i_func_call=i_func_call+1
           f_B=func01_aosc658c(x_sub_end)
           if(f_A*f_B.le.0.) then
             write(6,710)x_sub_beg,x_sub_end
710          format(/,'A Root Lies Between ',1PE13.6,' and ',1PE13.6)
C     +                  1PE13.6)             
             iroot=iroot+1
           endif  
           x_sub_beg=x_sub_end
           x_sub_end=x_sub_beg+delta_x
        enddo
        write(6,750)i_func_call
750     format(/, 'Number of function calls =',I17)        

        end

        function func01_aosc658c(x)
        implicit double precision(a-h,o-z)

        func01_aosc658c=cos(x)-x**2

        return
        end
