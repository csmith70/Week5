ab        program newton_raphson
        implicit double precision(a-h,o-z)
        external func01_aosc652

        xtol=1.d-2
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

        call rtnewt(func01_aosc652,x_beg,x_end,x_tol,i_func_call,
     +          x_root,f_root,nconv)

        write(6,750)x_root,f_root,i_func_call,nconv
750     format(/,'Root             =',1PE20.13,/,
     +           'Function of Root =',1PE11.4,/,
     +           'Function calls   =',I4,/,
     +           'Convergence flag =',I4)        

        stop
        end

        subroutine rtnewt(func,x_beg,x_end,x_tol,i_func_call,x_root,
     +          f_root,nconv)
C
C     Finds roots of "func" using bisection method
C     Based on subroutine rtnewt, page 358 of Press et al.
C
C     Inputs:
C             x_beg: beginning of interval
C             x_end: end of interval
C             x_tol: acccuracy (or tolerance) of root
C
C     Outputs:
C            i_func_call: number of calls to function "func"
C            x_root: root of function "func"
C            f_root: value of function evaluated at x_root
C            nconv: 0 for successful convergence
C                   1 for update to root jumping out of bounds
C                   2 for non convergance within jmax interations
C                   3 for non convergance due to first derivative=0
C                  99 for some type of program failure

        implicit double precision(a-h,o-z)
        external func
        parameter(jmax=40)

        nconv=99        ! Initialize with value that indicates some type of failure
        x_root=-999.d0  ! Initialize to our value of "NA"
        i_func_call=0   ! Initialize number of function calls
        delta_x=1.d38   ! Initialize at large number to assure that the
                        ! "do while" loop is entered the first time through

        x_root=0.5d0*(x_beg+x_end)
        jloop=0
        do while(abs(delta_x).gt.x_tol)
                i_func_call=i_func_call+1
                call func(x_root,f_root,df)
                if(df.ne.0.d0) then
                        delta_x=-f_root/df
                        x_root=x_root+delta_x
                else
                        nconv=3
                        write(6,700)
                        return
                endif
                jloop=jloop+1
                if(jloop.ge.jmax) then
                   nconv=2
                   return
                endif   
                if((x_root.lt.x_beg).or.(x_root.gt.x_end)) then
                   nconv=1
                   write(6,702)
                   return
                endif
        enddo
        if(abs(delta_x).le.x_tol) nconv=0       ! Converged

700     format('Derivative inside Newton Raphson = 0: ',
     +          'Convergence Failure')        

702     format('The update on "x" jumped out of bounds: ',
     +          'Convergence Failure')        

        return
        end

        subroutine func01_aosc652(x,f,df)
        implicit double precision(a-h,o-z)

        f=cos(x)-x**2   ! Function
        df=-sin(x)-2.d0*x   ! Derivative

        return
        end
