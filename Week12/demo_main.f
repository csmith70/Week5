	program demo

	real*8 a1,a2,a3,a4,a5,av1

	print *,'Enter five numbers: '
	read *,a1,a2,a3,a4,a5

	av1=avrage(a1,a2,a3,a4,a5)
	call average(a1,a2,a3,a4,a5,av2)

	print *,'average from function   is :',av1
	print *,'average from subroutine is :',av2

	stop
	end
