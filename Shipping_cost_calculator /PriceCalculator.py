 #Sal's Shipping
# Sonny Li

weight = 41.5

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("🚚💨 \nGround Shipping: \n$",cost_ground)
      
# Ground Shipping Premimum 🚚💨

cost_ground_premium = 125.00

print("\n🚚💨\nGround Shipping Premimium: \n$", cost_ground_premium)

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("\n🛸\nDrone Shipping: \n$", cost_drone)


