! Christopher Smith
! HW16: FORTRAN Running Mean and Root Finding
! November 18, 2019
      implicit none
      real :: i, rdopst, wropst, rdst
      character(30) :: rdfile, wrfile
      character(132) :: line
      do
      write (*,'(a)', advance="no") "Input File Name: "
      read (*,*) rdfile
      open(12, file=rdfile, status="old", 
     +action="read", position="rewind")
      if (rdopst==0) exit
      write (*,'(a/,a)') "Unable to open input file.",
     + "Please re-enter"
      end do
      do
      write (*,'(a)', advance="no") "Output File Name: "
      read (*,*) wrfile
      open(14, file=wrfile, status="replace", 
     +action="write", position="rewind")
      if (wropst==0) exit
      write (*,'(a, a/,a)') "Unable to open ", 
     +"output file.", "Please re-enter"
      end do
      i = 1
      do
! read line from input file
      read (12, '(a)') line
! if end of file, exit loop
      if (rdst >0) stop "read error"
      if (rdst <0) exit 
! write line number and line to output file
      write (14, '(i10,2x,a)')line
      i = i + 1
      end do
! close files
      close(12)
      close(14)
      end program 
