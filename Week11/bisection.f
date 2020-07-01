        program bisection
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
        read(5,*)x_tol

        call rtbis(func01_aosc658c,x_beg,x_end,x_tol,i_func_call,x_root,
     +          nconv)

        write(6,750)x_root,i_func_call,nconv
750     format(/,'Root             =',1PE13.6,/,
     +           'Function calls   =',I4,/,
     +           'Convergence flag =',I4)        

        stop
        end

        subroutine rtbis(func,x_beg,x_end,x_tol,i_func_call,x_root,
     +          nconv)
C
C     Finds roots of "func" using bisection method
C     Based on subroutine rtbis, page 347 of Press et al.
C
C     Inputs:
C             x_beg: beginning of interval
C             x_end: end of interval
C             x_tol: acccuracy (or tolerance) of root
C
C     Outputs:
C            i_func_call: number of calls to function "func"
C            x_root: root of function "func"
C            nconv: 0 for successful convergence
C                   1 for no root found in interval
C                   2 for non convergance within jmax interations
C                  99 for some type of program failure

        implicit double precision(a-h,o-z)
        external func
        parameter(jmax=2000)

        nconv=99        ! Initialize with 
        x_root=-999.    ! Initialize to our value of "NA"
        i_func_call=0   ! Initialize number of function calls

        i_func_call=i_func_call+1
        f_beg=func(x_beg)
        i_func_call=i_func_call+1
        f_end=func(x_end)
        
        if(f_beg*f_end.gt.0.) then
           nconv=1
           write(6,700)
700        format('func(x_beg)*func(x_end) > 0, implying either ',
     +          ' multiple roots or no root',/,
     +          'Please revise search boundaries')
           return
        endif
        if(f_beg.lt.0.) then
           x_root=x_beg
           delta_x=x_end-x_beg
        else
           x_root=x_end
           delta_x=x_beg-x_end
        endif
        jloop=1
        do while(abs(delta_x).gt.x_tol)
          delta_x=0.5*delta_x
          x_end=x_root+delta_x
          i_func_call=i_func_call+1
          f_end=func(x_end)
          if(f_end.le.0.) x_root=x_end
          if(f_end.eq.0.) then                  ! Converged
                nconv=0
                return
          endif      
          jloop=jloop+1
          if(jloop.ge.jmax) then
             nconv=2
             return
          endif
        enddo
        if(abs(delta_x).le.x_tol) nconv=0       ! Converged

        return
        end

        function func01_aosc658c(x)
        implicit double precision(a-h,o-z)

        func01_aosc658c= 4.02805505e-07*x**(3) - 2.27802702e-03*x**(2) 
     +  +  4.29570531e+00*x - 2.70126799e+03

        return
        end
