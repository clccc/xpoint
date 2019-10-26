#coding:utf-8
#-----------------------------
#code by Chenlin 2017-02-19 21:48:24
#displaydata ConvertedDatapath datastructname  functionname
#
#-----------------------------

import sys
sys.path.append("..")
import commonFile.DataStruct as DataStruct
import commonFile.DataStruct_D as DataStruct_D
import commonFile.DataStruct_M as DataStruct_M
import commonFile.OPS_DataStruct as OPS_DataStruct
from commonFile.ObjDataAndBinFile import ObjDataAndBinFile


class displaydata:
    def run(self, converteddatapath, datastructname,functionname):
        print "\n*************  %s  by %s***************\n"%(functionname,datastructname)
        objfile = ObjDataAndBinFile()
        dbcalls = objfile.binfile2objdata(converteddatapath)
        call_obj = None
        #默认输出结构体的第一层的结构是一致
        if("1" == functionname):
            call_obj = dbcalls.callinfolist
        else:
            for call in dbcalls.callinfolist:
                    if(call.call_code == functionname):
                        call_obj = call
                        break

        if call_obj == None:
            print "没有该函数的信息!\n"
            return

        if datastructname == "DataStruct_M":
            self.trans_by_DataStruct_M(call_obj)
            return
        if datastructname == "DataStruct_D":
            self.trans_by_DataStruct_D(call_obj)
            return
        if datastructname == "DataStruct_intrap":
            self.trans_by_DataStruct_intrap(call_obj)
            return
    '''
    #按DataStruc_M 解析call的内部信息
    def trans_by_DataStruct_M(self,call):
        s_out = ""
        s_out += "%s[%s] : ID = %s\n"%(call.call_code,call.callsiteNums,call.call_id )
        i=0
        for callsite in call.callsiteinfolist:
            s_out += " %4d) "%i
            s_out += "\'%s\' ID = %d\n"%(callsite.callsite_code,callsite.callsite_id)
            j=0
            for arg in callsite.callsite_argsinfolist:
                s_out += "\t arg%2d : "%j
                s_out += "\'%s\' ID = %d\n"%(arg.arg_code,arg.arg_id)
                s_out += "\t\targ_condidlist = %s\n"%arg.arg_condidlist
                s_out += "\t\targ_stmtsleftlist = %s\n"%arg.arg_stmtsleftlist
                s_out += "\t\targ_stmtsrightlist = %s\n"%arg.arg_stmtsrightlist
                s_out += "\t\targ_stmtiscalllist = %s\n"%arg.arg_stmtiscalllist
                j=j+1
            i = i+1
        print s_out

    #按DataStruc_D 解析call的内部信息
    def trans_by_DataStruct_D(self,call):
        s_out = ""
        s_out += "%s[%s] : ID = %s\n"%(call.call_code,call.callsiteNums,call.call_id )
        i=0
        for callsite in call.callsiteinfolist:
            s_out += " %4d) "%i
            s_out += "\'%s\' ID = %d\n"%(callsite.callsite_code,callsite.callsite_id)
            j=0
            for arg in callsite.callsite_argsinfolist:
                s_out += "\t arg%2d : "%j
                s_out += "\'%s\' ID = %d\n"%(arg.arg_code,arg.arg_id)
                s_out += "\t\targ_condidlist = %s\n"%arg.arg_condidlist
                s_out += "\t\targ_stmtsleftlist = %s\n"%arg.arg_stmtsleftlist
                s_out += "\t\targ_stmtsrightlist = %s\n"%arg.arg_stmtsrightlist
                s_out += "\t\targ_stmtiscalllist = %s\n"%arg.arg_stmtiscalllist
                j=j+1
            i = i+1
        print s_out
    '''

    #按DataStruc_D 解析call的内部信息
    def trans_by_DataStruct_intrap(self,call):

        if(type(call) == list):
            for atomcall in call:
                s_out = ""
                s_out += "%s[%s] : ID = %s\n"%(atomcall.call_code,atomcall.callsiteNums,atomcall.call_id )
                i=0
                for callsite in atomcall.callsiteinfolist:
                    s_out += " %4d) "%i
                    s_out += "%s \'%s\' ID = %d\n"%(callsite.argcheckresult,callsite.call_code,callsite.call_id)
                    i = i+1
                print s_out
        else:
            s_out = ""
            s_out += "%s[%s] : ID = %s\n"%(call.call_code,call.callsiteNums,call.call_id )
            i=0
            for callsite in call.callsiteinfolist:
                s_out += " %4d) "%i
                s_out += "%s \'%s\' ID = %d\n"%(callsite.argcheckresult,callsite.call_code,callsite.call_id)
                i = i+1
            print s_out

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if len(sys.argv) != 4 :
        print ("displaydata ConvertedDatapath datastructname functionname\n")
    else:
        converteddatapath = sys.argv[1]
        datastructname = sys.argv[2]
        functionname = sys.argv[3]
        tool = displaydata()
        tool.run(converteddatapath,datastructname, functionname)

