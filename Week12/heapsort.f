        subroutine heapsort(n,ra)

        integer n
        integer i,ir,j,k

        real ra(n),rra
C
C            Sorts an array ra(1:n) into ascending numerical order using
C            the Heapsort algorithm.
C            n is input
C            ra is replaced on output by its sorted rearrangement.
C
C            Page 329, Press et al., Numerical Recipes in Fortran, 2nd Ed.

        if(n.lt.2) return       ! Nothing to sort
C
C            The index k will be decremented from its initial value down
C            to 1 during the "hiring" (heap creation) phase.  Once it
C            reaches 1, the index ir will be decremented from its
C            initial value down to 1 during the "retirement and
C            promotion" (heap selection) phase
C

        k=n/2+1
        ir=n
10      continue
          if(k.gt.1) then
                k=k-1
                rra=ra(k)
          else
                rra=ra(ir)
                ra(ir)=ra(1)
                ir=ir-1
                if(ir.eq.1) then
                   ra(1)=rra
                   return
                endif
          endif         
          i=k
          j=k+k
20        if(j.le.ir) then
             if(j.lt.ir) then
                if(ra(j).lt.ra(j+1)) j=j+1
             endif
             if(rra.lt.ra(j)) then
                ra(i)=ra(j)
                i=j
                j=j+j
             else
                j=ir+1
             endif
          goto 20
          endif
          ra(i)=rra
        goto 10
        return
        end
