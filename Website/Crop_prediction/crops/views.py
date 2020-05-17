from django.shortcuts import render


from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor






from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd


dataset = pd.read_csv(r'/home/akhtar/Desktop/Ml Algorithms/Dataset/crops.csv')
Districts= None
Area = None
Category = None
Crop =None
Year = None

def Rainfall_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Min_Temp','Humidity','Wind_Speed','Cloud_Coverage','Bright_Sunshine','ALT','Productions'], axis = 1)
     y_pred=None
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = RandomForestRegressor(n_estimators=20)
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pred = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pred


def Humidity_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Min_Temp','Rainfall','Wind_Speed','Cloud_Coverage','Bright_Sunshine','ALT','Productions'], axis = 1)
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = RandomForestRegressor(n_estimators=20)
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pre = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pre


def Altitude_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Min_Temp','Humidity','Wind_Speed','Cloud_Coverage','Bright_Sunshine','Rainfall','Productions'], axis = 1)
     y_pred=None
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = DecisionTreeRegressor()
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pred = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pred


def Bright_Sunshine_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Min_Temp','Humidity','Wind_Speed','Cloud_Coverage','Rainfall','ALT','Productions'], axis = 1)
     y_pred=None
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = RandomForestRegressor(n_estimators=20)
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pred = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pred



def Cloud_Coverage_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Min_Temp','Humidity','Wind_Speed','Rainfall','Bright_Sunshine','ALT','Productions'], axis = 1)
     y_pred=None
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = RandomForestRegressor(n_estimators=20)
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pred = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pred



def Min_Temp_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Rainfall','Humidity','Wind_Speed','Cloud_Coverage','Bright_Sunshine','ALT','Productions'], axis = 1)
     y_pred=None
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = RandomForestRegressor(n_estimators=20)
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pred = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pred



def Wind_Speed_Prediction(request): 
     dataset_12 = dataset.drop(['Max_Temp', 'X_COR', 'Y_COR', 'LATITUDE','LONGITUDE','Min_Temp','Humidity','Rainfall','Cloud_Coverage','Bright_Sunshine','ALT','Productions'], axis = 1)
     y_pred=None
     X = dataset_12.iloc[:, :-1]
     y = dataset_12.iloc[:, -1]

     # sc_X = StandardScaler()
     # sc_y = StandardScaler()
     # X = sc_X.fit_transform(X)
     # y = sc_y.fit_transform(y.values.reshape(-1,1))

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

     regressor = RandomForestRegressor(n_estimators=20)
     regressor.fit(X_train, y_train)

     if request.method == 'POST':
          District = request.POST['Districts']
          if District == 'Bandarban':
               Districts = 1 
          elif District == 'Barishal':
               Districts = 2  
          elif District == 'Bogra':
               Districts = 3  
          elif District == 'Chittagong':
               Districts = 4  
          elif District == 'Comilla':
               Districts = 5  
          elif District == 'Dhaka':
               Districts = 6      
          elif District == 'Dinajpur':
               Districts = 7  
          elif District == 'Faridpur':
               Districts = 8  
          elif District == 'Jamalpur':
               Districts = 9  
          elif District == 'Jessore':
               Districts = 10  
          elif District == 'Khagrachari':
               Districts = 11  
          elif District == 'Khulna':
               Districts = 12  
          elif District == 'kishoreganj':
               Districts = 13  
          elif District == 'Kushtia':
               Districts = 14  
          elif District == 'Mymensingh':
               Districts = 15  
          elif District == 'Noakhali':
               Districts = 16  
          elif District == 'Pabna':
               Districts = 17  
          elif District == 'Patuakhali':
               Districts = 18  
          elif District == 'Rajshahi':
               Districts = 19 
          elif District == 'Rangamati':
               Districts = 20
          elif District == 'Rangpur':
               Districts = 21 
          elif District == 'sylhet':
               Districts = 22
          elif District == 'Tangail':
               Districts = 23
          Area = request.POST['Area']
          Categor = request.POST['Category']
          if Categor == 'Broadcast':
               Category = 1 
          elif Categor == 'HYV':
               Category = 2        
          elif Categor == 'Local':
               Category = 3  
          elif Categor == 'Pajam':
               Category = 4  
          elif Categor == 'Hybrid':
               Category = 5                                        
          Cro = request.POST['Crop']
          if Cro == 'Aman':
               Crop = 1 
          elif Cro == 'Aus':
               Crop = 2            
          elif Cro == 'Boro':
               Crop = 3  
          elif Cro == 'Jute':
               Crop = 4  
          elif Cro == 'Potato':
               Crop = 5 
          elif Cro == 'Wheat':
               Crop = 6 

          Year = request.POST['Year']
          y_pred = float(regressor.predict([[Districts,Area,Category,Crop,Year]])) 
          return y_pred


def Recommendation(request):
     a = Humidity_Prediction(request) 
     b = Rainfall_Prediction(request)
     c = Altitude_Prediction(request)
     d = Bright_Sunshine_Prediction(request)
     e = Cloud_Coverage_Prediction(request)
     f = Min_Temp_Prediction(request)
     g = Wind_Speed_Prediction(request)
     return render(request, 'prediction.html', {'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g})
"""def index(request):
    dataset = pd.read_csv(r'/home/akhtar/Desktop/Crop Yield Prediction For Bangladesh/Crops.csv')
    linear = LinearRegression()
    linear.fit(dataset[['Districts','Area','Category','Crop','Year','Max-Temp','Min-Temp','Rainfall']], dataset.Productions)
    Districts= None
    Area = None
    Category = None
    Crop =None
    Year = None
    Max_Temp = None
    Min_Temp =None
    Rainfall =None
    score=None

    if request.method == 'POST':
         Districts = float(request.POST['Districts'])
         Area = float(request.POST['Area'])
         Category = float(request.POST['Category'])
         Crop = float(request.POST['Crop'])
         Year = float(request.POST['Year'])
         Max_Temp = float(request.POST['Max_Temp'])
         Min_Temp = float(request.POST['Min_Temp'])
         Rainfall =float(request.POST['Rainfall'])
         
         score = linear.predict([[Districts,Area,Category,Crop,Year,Max_Temp,Min_Temp,Rainfall]])
         #print(score)
         print() 
    return render(request, 'index.html',{'score':score})
    
def blog(request):
     return render(request, "blog.html")"""