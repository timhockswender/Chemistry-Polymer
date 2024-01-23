#
#
import matplotlib.pyplot as plt

def PlotResults (x_calc, y_calc, x_obs, y_obs, plot_array, T, Save_Plot):
    # Create the plot fro the conversion and actual exermental(observed) values
    #Additinally add aplot of the residuals calculated at each point
    #Create a figure area with two plots
    fig, (ax1, ax2) = plt.subplots(2, 1, height_ratios=[4,1], sharex=True)
    #ax1 = fig.add_subplot(1, 2, 1)
    #ax2 = fig.add_subplot(1, 2, 2)
    #plt.figure(figsize=(6, 5))  # Adjust figure size if needed
    #plot the results of the solution to the differential equation
    ax1.plot(x_calc, y_calc, label="Calculated", color="blue", alpha=0.7)
    
    # Plot observed data
    #plt.plot(x_obs, y_obs, label="Observed", color="red", marker='o')
    ax1.scatter(x_obs, y_obs , label="Observed", color="red", marker='o')
    # Customize the plot
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Conversion")
    ax1.set_title(f"Calculated vs Observed Data at Temperature = {T}")
    ax1.legend()
    ax1.grid(True)
    
     #Adjust x-axis limits to observed data range (optional)
    #plt.xlim(min(x_obs), max(x_obs))
    #plt.xticks(np.arange(0, max(x_calc), 50))
    #plt.xticks(np.arange(0, 18000))
    #plt.xticks(np.arange(0, max(x_calc), step=15000)) #96,000 seconds at 40 degrees
    #plt.xticks(np.arange(0, max(x_calc), step=1500)) #rescale at 70 degrees
    #plt.xticks(np.arange(0, 96000, step=15000)) #96,000 seconds at 40 degrees

    #plt.xticks(np.arange(0, tf , step= 15000 ) ) #rescale at 70 degrees
    ax1.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax1.twinx
    ax2.plot(x_obs, plot_array, color = 'blue', markerfacecolor = 'r',  marker ='D') 
    #ax2.plot(x_obs, y_obs, marker = 'o') 
    ax2.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax2.set_title(f"Residuals Calculated at Temperature = {T}")
    
    #ax2.set_ylim(min(plot_array), max(plot_array) )
    #ax2.axhline(y=0.0, xmin=0.0, xmax= max(x_obs), color='r') #doedn't add anything
    ax2.grid()
    plt.subplots_adjust(hspace=0.4)
    # Show the plot
    #plt.tight_layout()
    if Save_Plot:
        fn = 'Run_Temperature_' + str(T) + '.png'
        plt.savefig(fn, dpi=300)
    plt.show()
    
    return

def Plot_MandI (ode_result, T):
    #Create a figure area
    fig = plt.figure(figsize=(12,6))
    # Create two plots
    #fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    # Plot the first set of data
    # plt. gca()
    ax1.plot(ode_result.t, ode_result.y[1,:], label='Monomer', )
    ax1.set_ylabel('Concentration')
    ax1.set_xlabel('Time(s)')
    ax1.grid()
    ax1.set_title(f'Run Temperature = {T} ' )
    ax1.legend() #NOTE essential for the labels
    
    ax2.plot(ode_result.t, ode_result.y[0,:], label = 'Initiator')
    ax2.set_ylabel('Concentration')
    ax2.set_xlabel('Time(s)')
    ax2.grid()
    ax2.set_title(f'Run Temperature = {T} ' )
    ax2.legend()
    # Change the spacing between the plots
    # Increase the spacing between the plots
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.show()
    return
    
def Plot_Number_Average(sol):
    t = sol.t[1:]  #change index to avoid divide by zero at t=0
    num   = sol.y[3][1:] - sol.y[6][1:]
    denom = sol.y[2][1:] - sol.y[5][1:]
    #print(num.shape, t.shape)
    Wn = num/denom
    plt.plot( Wn, label='Number Average')
    plt.grid()
    plt.xlabel('Time (min)')
    plt.ylabel('Number Aveage ')
    plt.legend()
    plt.show()
    return Wn[-1]

def Plot_Number_Average(sol):
    t = sol.t[1:]  #change index to avoid divide by zero at t=0
    num   = sol.y[3][1:] - sol.y[6][1:]
    denom = sol.y[2][1:] - sol.y[5][1:]
    #print(num.shape, t.shape)
    Wn = num/denom
    plt.plot( Wn, label='Number Average')
    
    plt.grid()
    
    plt.xlabel('Time (min)')
    plt.ylabel('Number Aveage ')
    plt.legend()
    plt.show()
    return Wn[-1]

def Plot_Weight_Average(sol):
    t = sol.t[1:]  #change index to avoid divide by zero at t=0
    num   = sol.y[4][1:]
    denom = sol.y[3][1:]
    #print(num.shape, t.shape)
    Ww = num/denom
    plt.plot( Ww, label='Weight Average')
    #plt.plot( denom, label='Weight Average')
    plt.grid()
    plt.xlabel('Time (min)')
    plt.ylabel('Weight Aveage ')
    plt.legend()
    plt.show()
    return Ww[-1]

def Plot_Number_and_Weight_Averages(ode_result, T ):
    
        #Create a figure area with two plots
    fig = plt.figure(figsize=(12,4))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    # Plot the first set of data
    # plt. gca()
    #calculate Weight average
    
    times = ode_result.t[1:]  #change index to avoid divide by zero at t=0
    num   = ode_result.y[4][1:]
    denom = ode_result.y[3][1:]
    print('shapes are', num.shape, times.shape)
    Ww = num/denom
    ax1.plot(times, Ww, label='Weight Average Molecular Weight', )
    #plt.plot( denom, label='Weight Average')
    ax1.set_ylabel('Value')
    ax1.set_xlabel('Time')
    Ww_value = round(Ww[-1], 3)
    v_string = 'Wgt. Avg. MW ' + str(Ww_value)
    #ax1.text(2, 6, r'Wgt. Avg. MW: $E=mc^2$', fontsize=15)
    #ax1.text(2, 6, r'Wgt. Avg. MW: {Ww}', fontsize=8)
    #ax1.text(2, 6, r'Wgt. Avg. MW: $E=mc^2$', fontsize=8)
    #ax1.text(0.3, .5, 'Begin text', horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes)
    ax1.text(0.4, .52, v_string, horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes)
    ax1.grid()
    ax1.set_title(f'Run Temperature = {T} ' )
    ax1.legend() #NOTE essential for the labels
    num   = ode_result.y[3][1:] - ode_result.y[6][1:]
    denom = ode_result.y[2][1:] - ode_result.y[5][1:]
    Wn = num/denom
    Wn_value = round(Wn[-1], 3)
    v_string = 'Num. Avg. MW ' + str(Wn_value)
    print(v_string)
    ax2.text(0.4, .5, v_string, horizontalalignment='center', verticalalignment='center', transform=ax2.transAxes)
    ax2.plot(times, Wn, label='Number Average Molecular Weight', )
    ax2.set_ylabel('Value')
    ax2.set_xlabel('Time')
    ax2.grid()
    ax2.set_title(f'Run Temperature = {T} ' )
    ax2.legend()
    # Change the spacing between the plots
    # Increase the spacing between the plots
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.show()

    return Ww[-1], Wn[-1]
    
def Plot_Conversion(ode_result,  M0, T):
    conversion =1 - (ode_result.y[1,:]/M0 )
    plt.plot(ode_result.t, conversion, label='Conversion')
    plt.xlabel('Time (sec)')
    plt.ylabel('Fraction Converted')
    plt.title('Conversion')
    plt.legend()
    plt.grid()    
    
def Plot_2_Conversions(ode_result1, ode_result2, M0, T):
    fig = plt.figure(figsize=(12,6))
    # Create two plots
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    # Create and Plot the first set of data
    conversion1 =1 - (ode_result1.y[1,:]/M0 )
    ax1.plot(ode_result1.t,conversion1, label='Conversion[1]', )
    ax1.set_ylabel('Fraction Converted')
    ax1.set_xlabel('Time(sec)')
    ax1.grid()
    ax1.set_title(f'Run Temperature = {T} ' )
    ax1.legend() #NOTE essential for the labels
    conversion2 =1 - (ode_result2.y[1,:]/M0 )
    ax2.plot(ode_result2.t, conversion2, label = 'Conversion[2]')
    ax2.set_ylabel('Fraction Converted')
    ax2.set_xlabel('Time(s)')
    ax2.grid()
    ax2.set_title(f'Run Temperature = {T} ' )
    ax2.legend()
    # Change the spacing between the plots
    # Increase the spacing between the plots
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.show()
    return
def Plot_Conversion_Hours(ode_result, M0, T):
    conversion =1 - (ode_result.y[1,:]/M0 )
    x =  ode_result.t/3600
    plt.plot( x, conversion, label='Conversion')
    plt.xlabel('Time (hours)')
    plt.ylabel('Fraction Converted')
    plt.title('Conversion')
    plt.legend()
    plt.grid()    

def Plot_AKS_Conversion_Versus_Chain_Length(ode_result, M0, T):
    conversion =1 - (ode_result.y[1][1:]/M0 )
    Xn = ode_result.y[3][1:]/ode_result.y[2][1:]  #avoid divide by zero at time 0
    plt.plot( conversion, Xn,  label='Length'  )
    plt.ylabel ('Chain Length' )
    plt.xlabel('Conversion')
    plt.title( 'Conversion versus Chain Length')
    plt.legend()
    plt.grid()    



def Plot_All_Moments(ode_result, title):
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))  # Create a figure with 2 rows and 3 columns
    
    for z in range(1, 7):
        ax = axes.flat[z - 1]  # Get the corresponding subplot axis
        ax.plot(ode_result.t[1:], ode_result.y[z][1:])
        ax.set_title(f"Moment {z} ")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.grid()
    
    fig.suptitle("Moments from " + title, fontsize=16)  # Set the overall title
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()
    return

def Plot_Conversions_Versus_Chain_Length(ode_result1,ode_result2 , M0, T):
    conversion =1 - (ode_result1.y[1][1:]/M0 )
    #Lambda1 / Lambda 0
    Xn_AKS = ode_result1.y[3][1:]/ode_result1.y[2][1:]  #avoid divide by zero at time 0
    Xn_Dhooge =  ode_result2.y[6][1:]/ode_result2.y[5][1:]  #avoid divide by zero at time 0
    plt.plot( conversion, Xn_AKS,  label='AKS'  )
    plt.plot( conversion, Xn_Dhooge,  label='Dhooge'  )
    plt.ylabel ('Chain Length' )
    plt.xlabel('Conversion')
    plt.title( 'Conversion versus Chain Length')
    plt.legend()
    plt.grid()    
    plt.show()
    return

