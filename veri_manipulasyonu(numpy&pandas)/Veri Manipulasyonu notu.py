from operator import concat
import numpy as np
import pandas as pd
import seaborn as sns

                                                            #NUMPY

#Np Array oluşturma: Array özelliği sadece tek tip değerler tutar. Sadece int gibi. Extra listedeki elemanların indexinide tutar.
np.array([1,2,3,4,5,6]) ;        a = np.array([1,3,4,5,6,7]) ;          b =np.array([3.14, 4, 2, 13], dtype = "int")    #b'de arrayin tipini intager yaptık. 


#0'dan Array oluşturma otomatik olarak.
x=np.zeros(10, dtype="int");       y=np.ones(10, dtype="int");     z=np.full((3,5),3) #x'de 0'lı 10 eleman oluştu. y'de 1'li. z'de 3satır 5 sutun lu 3lerden oluşan array.
a=np.arange(0,31, 3);           b=np.linspace(0,1,10); #a:0 ile 30 arası 3 er arttır , b:0-1 arası 10 sayı        
c=np.random.normal(10, 4, (3,4));            d = np.random.randint(0,10, (3,3))    #c:ortalaması 10, stan.s 4 , 3-4 lük sayı ,  d: 0-10 arası 3-4lük random değerler oluşturuldu.


#Array özellikleri
x = np.random.randint(10, size = 10);       x.ndim  ;      x.shape;     x.size;     x.dtype;
#    ndim:boyut sayısı     shape: boyut bilgisi         size: toplam eleman sayısı          dtype: array veri tipi


#Yeniden Şekillendirme(Reshaping)
a = np.arange(1,10).reshaping((3,3)) #1'den 10 a kadar elemanları 3-3lük array haline getirir.


# Array Birlestirme (Concatenation)
x = np.array([1,2,3]) ;     y = np.array([4,5,6]) ;         np.concatenate([x, y]) #a ve b arrayleri birleştirir.
a = np.array([[1,2,3],[4,5,6]]) ;      np.concatenate([a,a], axis = 1)  #2 boyutluda birleştirme yapıldı. axis:1 sutun bazında birleştirme , 0 olduğunda satır bazında birleşir.


# Array Ayırma (Splitting)
x = np.array([1,2,3,99,99,3,2,1]);      a,b,c = np.split(x, [3,5]);  #1,2,3:a  99,99:b  3,2,1:c


#Array Sıralama(Sorting)
v = np.array([2,1,4,3,5]);      x=np.sort(v);     v.sort; #sort'un iki kullanımı vardır. v nin sıralanmısı x e atar. v aynı kalır. 2.de ise v sıralanır orjinali.


#İndex ile elemana ulaşma sistemi
m = np.random.randint(10, size = (3,5)) ;   m[0,0]  ; m[2,3] #İki boyutlu sistemde 2.satır 3.sutundaki elemana vs bu sekilde ulaşılabilir.
a = np.arange(20,30) ;  a[0:3] ; a[1::2] #Bu şekilde 0. elemandan 3. elemana kadar getir veya 1.elemandan başla sonuna kadar 2şerli git işlemi.
m = np.random.randint(10, size = (5,5)) ;  m[1:3, 0:2] # Bu şekilde 2 boyutlu 1.ve 2. satırı al, sutundan 0. ve 1. sutunu al demiş olduk.


# Slicing ile Elemanlara Erişmek (Array Alt Kümesine Erişmek)
a = np.arange(20,30);       a[0::3] #0. indexten başla 3'er arttırarak arrayi yaz. 2 boyutluda olsa virgül koy araya.


# Alt Küme Üzerinde işlem yapma.
m = np.random.randint(10, size = (5, 5));       alt_b = m[0:3, 0:2].copy(); #copy ile seçilen alt küme ana kümeden bağımsızlaşır.


# Fancy Index ile Elemanlara Erişmek
v = np.arange(0, 30, 3) ;       [v[1], v[3], v[5]] #1,3 ve 5. indexe ulaşılır.

"""**********************************************************************************************************************************************************************************
*********************************************************************************************************************************************************************************"""



                                                #Pandas Kütüphanesi
#Pandas Serisi Oluşturma
pd.Series([10,88,3,4,5]);  #Pandas serileri elemanlarla birllikte index numarasıda tutar.
a = pd.Series([99,22,332,94,5], index = [1,3,5,7,9]) #Bu şekilde index numaramızı kendimize göre ayarlayabiliriz.
pd.concat([a,a]) # Bu şekilde seriler birleştirilir.

#Eleman İşlemleri
a[0:3];         list(a.items()) #1. de istediğimiz elemanları getiririz. 2.de bütün elemanları daha farklı gösterimle gelir karsımıza.


#Pandas DataFrame Oluşturma.
pd.DataFrame(a, columns = ["degisken_ismi"])    #Şeklinde dataframe oluşturulur.
df = pd.DataFrame(a, columns = ["var1","var2","var3"]);        a.head(1);       a.tail(1); #Dataframe oluşturduk. 1.Baştan , 2.Sondan eleman sayısını yazar.


#Eleman İşlemleri
a.index = ["a","b","c","d","e"] ;     a["c":"e"];      a.drop("a", axis = 0);         a["var4"] = a["var1"] / a["var2"];        a.drop("var4", axis = 1)     
#İndexleri arasında işlem yapılabilir. Drop:Silme işlemi gerçekleştirir.


# Gözlem ve Değişken Seçimi: loc & iloc
m = np.random.randint(1,30, size = (10,3));         df = pd.DataFrame(m, columns = ["var1","var2","var3"]);     df.loc[0:3];    df.iloc[0:3]    
#Burada loc'da 0'dan başlayıp 3ü dahil eder. İloç bizim alışık olduğumuz index mantıgı yani 0 ile 2 ye kadar olanları alır. 3 ü almaz.


#İşlemler
df[0:2][["var1","var2"]];    df.drop("a", axis = 0);        df.drop("a", axis = 0, inplace = True); #Drop ile eleman siliyoruz. 2.şekilde inplace ile kalıcı olarak silinir(index)
l = ["c","e"];      df.drop(l, axis = 0); #fancy ile eleman silme.
df.drop("var3", axis = 1)   #Şeklinde değişkenlerle silme işlemi yapılabilir.


#Karmasık
l = ["var1","var4","var2"];     #for i in l: print(i in df) Şeklinde sorgulama yapılabilir. True False True değeri gösterecektir.
df["var4"] = df["var1"] / df["var2"];       #Yeni bir tane var4 oluşturup 1 ile 2 nin bölümünden oluşur.


#İşlemler:
m = np.random.randint(1,30, size = (10,3));     df = pd.DataFrame(m, columns = ["var1","var2","var3"]);  #Yeni Dataframe Tanımlama 
df[df.var1 > 15];       df[(df.var1 > 15) & (df.var3 < 5)];                         #1.de var1 i 15 den yüksek olan degerler gelir. 2.benzer sistem vardır.
df.loc[(df.var1 > 15), ["var1","var2"]];     df[(df.var1 > 15)][["var1","var2"]]    #Değişken seçmek istersek 2 farklı şekilli kullanımı var.


#Birleştirme (Join) işlemleri
m = np.random.randint(1,30, size = (5,3));     df1 = pd.DataFrame(m, columns = ["var1","var2","var3"]);     df2 = df1 + 99  #df1 ve df2 yi tanımladık.
pd.concat([df1,df2]);       pd.concat([df1,df2], ignore_index=True) #1. de index 0123401234 şeklinde giderken 2.de 123456789 şeklinde gider.
df2.columns = ["var1","var2","deg3"]    #Şimdi var3 ü değ3 yaptık. Şimdi değişkenler farklı.
pd.concat([df1, df2], join = "inner") #İkisinin kesişimlerini getirir. Yani sadece var1 ve var2 yi.
pd.concat([df1, df2], join_axes = [df2.columns], ignore_index=True) #var1,var2,deg3 'ü getirir. df1 in deg3 degeri NaN yazar.


#İleri Birleştirme
df1 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'],'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'İK']})
df2 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'],'ilk_giris': [2010, 2009, 2014, 2019]})
pd.merge(df1, df2) # 4-4 birleştirme.(Eş bazlı)


# Toplulaştırma ve Gruplama (Aggregation & Grouping)
import seaborn as sns
#count()     first()     last()      mean()      median()        min()       max()       std()       var()       sum()
df.describe().T ;       df.dropna().describe().T     # Çoğunu toplu gösterir. T ile satır ve sutunların yeri değişir. 2.de ise - değerleri silerek işlem yaptı(dropna)


#Gruplama İşlemleri:
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],'veri': [10,11,52,23,43,55]}, columns=['gruplar', 'veri'])
df.groupby("gruplar").sum(); # gruplara göre grupladık , Sadece 1 tane A B C var. Karşılık gelen değerleri toplamasını istedik.
df.groupby("method")["orbital_period"].describe() # Grup içinde grup istersen bu şekilde kullanımda vardır.


# İleri Toplulaştırma İşlemleri (Aggregate, filter, transform, apply):
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'], 'degisken1': [10,23,33,22,11,99], 'degisken2': [100,253,333,262,111,969]}, columns = ['gruplar', 'degisken1', 'degisken2'])
#Aggregate:
df.groupby("gruplar").aggregate([min, np.median, max]);         df.groupby("gruplar").aggregate({"degisken1": "min", "degisken2": "max"}) #Şeklinde istediğimizi çağırırırız.
#Filter:
def filter_func(x): return x["degisken1"].std() > 9 ;   df.groupby("gruplar").filter(filter_func) #Şeklinde fonksiyonla istediğimiz işlemi yaptırabiliriz.
#transform:
df.transform(lambda x: (x-x.mean()) / x.std()) #Şeklinde isimsiz fonksiyonda kullanılabilir.
#apply
df.groupby("gruplar").apply(np.mean);           df.apply(np.mean); # Apply içine kütüphane fonk. çağrılabilir.



#Pivot Tablolar:
titanic = sns.load_dataset('titanic') # örnek veri
titanic.groupby("sex")[["survived"]].mean() #Burada zaten gruplama işleminin ortalamasını almıs
titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack() ; # Cinsiyet ve sınıfa göre sınıflayıp hayatta kalanların ortalamasını al , unstack ise tablo görselini değiştirir(daha iyi)
titanic.pivot_table("survived", index = "sex", columns = "class") # Yukarıdaki yerine buda yazılabilir..
#*********************************************************************Parçalama
age = pd.cut(titanic["age"], [0, 18, 90]) #Yaşı 0 , 18, 90 olarak böl
titanic.pivot_table("survived", ["sex", age], "class") #0-18 ile 18-90 yaş aralığını ayırıp işlem yaptık 


#Dış Kaynaklı Veri Okuma
pd.read_csv("reading_data/ornekcsv.csv", sep = ";") #İlk uzantı yolu işaret ederken sep ile yaptığımız ; kısmını kaldırdık
pd.read_csv("reading_data/duz_metin.txt") #txt okuma
pd.read_excel("reading_data/ornekx.xlsx") #Exel okuma

#Bonuss
#stack over ile karşılaşılan problemler yanıtlanabilir. Bir hatada en alttaki sorun sorunun özeti anlamına gelir.
#pandas documation yazıp sayfasına gidip orjinal içerikler inceleyebilirsin.











