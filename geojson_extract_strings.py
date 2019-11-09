"""
Daniel Bitters 2018

This program extracts state data from a Json file using iterations and string sequences.  

Data to be extracted are:
    1) state FIPS code
    2) state names
    3) the following statistics:
        - Longitude Max
        - Longitude Min
        - Latidue Max
        - Latitude Min

"""
    

def extract_state_data(file):
    
    import re

    #filein = open("c:/VSProjects/states.json", 'r')
    filein = open(file, 'r')
    stringin= filein.read()
    filein.close()

    count=0
    start=0
    index=0
    index_fips=0
    index_coords=0
    while(index!=-1):
        index=stringin.find("STATE_NAME",start)
        index_fips=stringin.find("STATE_FIPS",start)
        index_coords=stringin.find("coordinates",start)


        #extract each state's coordinates in string format
        coords= stringin[index_coords+15:stringin.find("]]}",index_coords)]
        #convert the string to a list of coordinates
        coords_list=re.findall(r'\[([^]]*)\]',coords)
        final_coords_list=[i.split(',')for i in coords_list]

        #find stats of latitude and longitude 
        long_list=[]
        lat_list=[]
        coords_index=0
        if(index!=-1):
            for x in final_coords_list:
                latitude=float(final_coords_list[coords_index][0])
                longitude=float(final_coords_list[coords_index][1])
                #new lists full of latitudes or longitudes only
                lat_list.append(latitude)
                long_list.append(longitude)
                coords_index=coords_index+1

            max_lat=(max(lat_list))
            min_lat=(min(lat_list))

            max_long=(max(long_list))
            min_long=(min(long_list))
        

        #extract state names
        state_name= stringin[index:stringin.find(",",index)]
        #extract state FIPS code
        state_fips= stringin[index_fips:stringin.find(",",index_fips)]

        start=index+1
        count=count+1


        if (index!=-1):
            print("State name:", state_name[12:])
            print("State FIPS code:",state_fips[12:])
            print("Longitude Minimum:",min_long)
            print("Longitude Maximum:",max_long)
            print("Latitude Minimum:",min_lat)
            print("Latitude Maximum:",max_lat)
            print("\n")
        
        

       
extract_state_data("c:/VSProjects/states.json")
        
       
        
    
