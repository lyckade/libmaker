import os
class Libmaker():
    
    def __init__(self,xpPath,sceneryName,libPrefix):
        """
        @param xpPath: Path to the X-Plane installation
        @param sceneryName: the path to the scenery folder
        @param libPrefix: the prefix for the definition of the virtual path
        @type xpPath: string
        @type sceneryName: string
        @type libPrefix: string
        """
        
        self.xpPath         = xpPath
        self.sceneryName    = sceneryName
        self.libTxtFileName = "librar.txt"
        self.libPrefix      = libPrefix
        
        #=======================================================================
        # If you want to make a extern Library definition you can add a prefix
        # to the realPath of the object
        #=======================================================================
        self.realPathPrefix = ""
        
        self.sceneryPath    = "%s/Custom Scenery/%s" % (self.xpPath,self.sceneryName)
        
        #=======================================================================
        # Definition of the different object types of x-plane
        # Just the filetype is defined.
        #=======================================================================
        self.objectTypes    = [ 
                               "obj",
                               "for",
                               "ags",
                               "fac",
                               "lin",
                               "pol"]
        #=======================================================================
        # The header is defined by each line. Easier to add and no need to 
        # define other files
        #=======================================================================
        self.header         = [
                               "A",
                               "800",
                               "LIBRARY",
                               ""]
        
    def makeLibrary(self):
        """
        The library.txt file is generated with that method
        """
        #------------------------------------------ Instance for the output file
        outputFile = open("%s/%s" % (self.sceneryPath,self.libTxtFileName),"w")
        #------------------------------------------------------ write the header
        for line in self.header:
            outputFile.write("%s\n" % (line))
        #------------------------------------------------- Loop over all folders
        packageContent = os.walk(self.sceneryPath)
        for folder in packageContent:
            for fileName in folder[2]:
                fileType = fileName.split(".")[-1]
                if fileType in self.objectTypes:
                    realPath = folder[0][len(self.sceneryPath)+1:].replace("\\","/")
                    filePath = "%s/%s" % (realPath,fileName)
                    print filePath
                    outputFile.write("EXPORT %s%s %s%s\n" % (self.libPrefix,filePath,self.realPathPrefix,filePath))
        outputFile.close()                    
            
    
    def setLibTxtFileName(self,libTxtFileName):
        """
        Method to specify another output file. The default is the library.txt file.
        @param libtTxtFileName:  the new name of the output file. 
        @type libTxtFileName:    string
        """
        self.libTxtFileName = libTxtFileName
        