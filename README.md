#Road Rage

Create a simulation of traffic on a road and find the optimal speed limit for the road.

##Challenge
1 kilometer section of road being built and we do not know what the speed limit needs to be. Simulate 1 kilometer of road to find the road speed. The optimal speed limit is one standard deviation above the mean speed.

##Assumptions
 - **Drivers**
	 - **Default Driver**
		 - Wants to go up to 120 km/hr.
		 - Want at least a number of meters equal to their speed in meters/second between them and the next car.
		 - Will accelerate 2m/s up to desired speed as long as they have room
		 - If a driver would hit another car by continuing, the stop
		 - Will randomly (10% chance each second) slow by 2 m/s. 
	 - **3 types of drivers**:
		 - *Normal*
			 - Acceleration - 2/m/s/s
			 - Desired Speed - 120 km/h
			 - Vehicle Size - 5m
			 - Minimum Spacing - speed
			 - Slowing Chance - 10%/s
			 - % of driver population - 75%
		 - *Aggressive*
			 - Acceleration - 5 m/s/s
			 - Desired Speed - 140 km/h
			 - Vehicle Size - 5m
			 - Minimum Spacing - speed
			 - Slowing Chance - 5%/s
			 - % of driver population - 10%
		 - *Commercial*
			 - Acceleration - 1.5 m/s/s
			 - Desired Speed - 100 km/h
			 - Vehicle Size - 25 m
			 - Minimum Spacing - 2x speed
			 - Slowing Chance - 10%/s
			 - % of driver population - 15%
	 - **Car**
		 - Average car is 5 meters long.
	 - **Roads**
		 - 2 Types:
			 - *Default*
				 - long one lane highway
				 - treated as a circle to represent constant traffic
			 - *Curvy*
				 - Kilometer 1: straight.
				 - Kilometer 2: slight curve. 40% higher slowing chance.
				 - Kilometer 3: straight.
				 - Kilometer 4: curve. 100% higher slowing chance.
                 - Kilometer 5: straight.
                 - Kilometer 6: slight curve. 20% higher slowing chance.
                 - Kilometer 7: straight.
		 - **Road Population**
			 - 30 cars per kilo evenly spaced
