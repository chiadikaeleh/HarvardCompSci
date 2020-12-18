# library to do some animations

# assumes you want to do a x/y plot and an energy plot

# empty placeholders for different plots
def plot_animations(fig, ax, t, E, r, l, s):
    
    nFrames = len(t) #number frames in our animation
    n_part = r.shape[0] #number particles

    # initialize our plots with empty data
    trajs = []
    for i in range(n_part):
        tr, = ax[0].plot([], [], linewidth=l, linestyle= s )
        # real one : tr, = ax[0].plot([],[], color=color, linewidth=linewidth)
        trajs.append(tr)

    energy, = ax[1].plot([],[], linewidth=l, linestyle= s )
    


    # set bounds based on data
    ax[0].set_xlim(r.min(), r.max())
    ax[0].set_ylim(r.min(), r.max())

    ax[1].set_xlim(t.min(),t.max())
    ax[1].set_ylim(E.min(),E.max())

    # names
    ax[0].set_xlabel('x in AU', fontsize=20)
    ax[0].set_ylabel('y in AU', fontsize=20)
    # energy
    ax[1].set_xlabel('Time in seconds', fontsize=20)
    ax[1].set_ylabel('Normalized Energy', fontsize=20)

    # below are functions animation.FuncAnimation needs
    # we need to initialize stuff - just setting data
    def init():
        # multiple planets
        for trajectory in trajs:
            #print(trajectory)
            trajectory.set_data([],[])

        energy.set_data([], [])

        # note: we have to do some special formatting to 
        #  get the correct output form for animate function
        outarr = trajs.copy()
        outarr.append(energy)
        return tuple(outarr)

    # now, each time we step through
    def animate(i):
        for j,trajectory in enumerate(trajs):
            trajectory.set_data(r[j,0,:i], 
                                 r[j,1,:i])

        energy.set_data(t[:i], E[:i])

        # note: we have to do some special formatting to 
        #  get the correct output form for animate function    
        outarr = trajs.copy()
        outarr.append(energy)
        return tuple(outarr)

    return init, animate, nFrames
