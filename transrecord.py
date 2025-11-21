import sys
if len(sys.argv)==6:
    stdname=sys.argv[1]
    busnum=sys.argv[2]
    pickuppoint=sys.argv[3]
    drivernum=sys.argv[4]
    print("User given input")
else:
    print("Input not given--default values taken")
    stdname="Darshan"
    busnum= "0506"
    pickuppoint="bvb"
    drivernum="9900852961"
    print("Student Name:"stdname)
    print("Bus Number:"busnum)
    print("Pick Up Point:"pickuppoint)
    print("Driver Phone Number:"drivernum)
