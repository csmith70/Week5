	program format_example

	character*6 cdate

100	continue
	write(6,700)
700	format('Enter date (YYMMDD) ... 999999 to end : ',$)
	read(5,*)cdate
	if(cdate.eq.'999999') goto 999

	write(6,704)
704	format('Enter latitude (deg, min, sec): ',$)
	read(5,*)xlat_deg,xlat_min,xlat_sec

	xlat=xlat_deg+xlat_min/60.+xlat_sec/3600.
	write(6,702)cdate,xlat
702	format(/,'cdate =',A6,' Lat (decimal degrees) =',F9.4,//)

	goto 100

999	continue

	stop
	end
