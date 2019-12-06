import json
import csv
import pandas as pd

# season 1

from pprint import pprint



def mainClass():
    # '../datafile/season14-15/season_match_stats.json'

    vard = {}
    vart = json.dumps(vard)


    def main():
        ficheros = ["../datafile/season14-15/","../datafile/season15-16/","../datafile/season16-17/",
                    "../datafile/season17-18/"]
        jsontocsv("validfinal.json")

        #seasonid =0
        #for dirname in ficheros:
        #   seasonid = parseojson(dirname,seasonid)


    def parseojson(season,seasonid):
        global_idpartidos = seasonid

        dirm = season+"season_match_stats.json"
        dirs = season+"season_stats.json"
        with open(dirm) as match:
            datamat = json.load(match)
        with open(dirs) as matchstat:
            datastats = json.load(matchstat)
        # la idea primera es añadir a matach cada extrastats
        idt = ["",""]
        for id in datamat:
                punt = 0
                for idtema in datastats[id]:
                    idt[punt] = idtema
                    punt = punt+1
                dataone = ajustdata(datastats,idt[0],id)
                datatwo = ajustdata(datastats, idt[1], id)
                final = result(datamat[id]['full_time_score'])
                matcjob = {
                    global_idpartidos: {
                        "season": season[-6:-1],
                        "home_team_id": datamat[id]['home_team_id'],
                        "away_team_id": datamat[id]['away_team_id'],
                        "home_team_name": datamat[id]['home_team_name'],
                        "away_team_name": datamat[id]['away_team_name'],
                        "date_string": datamat[id]['date_string'],
                        "half_time_score": datamat[id]['half_time_score'],
                        "full_time_score": datamat[id]['full_time_score'],
                        "full_time_result": final,
                        "home_att_goal_low_left": dataone[0],
                        "home_won_contest": dataone[1],
                        "home_possession_percentage": dataone[2],
                        "home_total_throws": dataone[3],
                        "home_att_miss_high_left": dataone[4],
                        "home_blocked_scoring_att": dataone[5],
                        "home_total_scoring_att": dataone[6],
                        "home_att_sv_low_left": dataone[7],
                        "home_total_tackle": dataone[8],
                        "home_att_miss_high_right": dataone[9],
                        "home_aerial_won": dataone[10],
                        "home_att_miss_right": dataone[11],
                        "home_att_sv_low_centre":dataone[12],
                        "home_aerial_lost": dataone[13],
                        "home_accurate_pass": dataone[14],
                        "home_total_pass": dataone[15],
                        "home_won_corners": dataone[16],
                        "home_shot_off_target": dataone[17],
                        "home_ontarget_scoring_att": dataone[18],
                        "home_goals": dataone[19],
                        "home_att_miss_left": dataone[20],
                        "home_fk_foul_lost": dataone[21],
                        "home_att_sv_low_right": dataone[22],
                        "home_att_goal_low_centre": dataone[23],
                        "away_att_goal_low_left": datatwo[0],
                        "away_won_contest": datatwo[1],
                        "away_possession_percentage": datatwo[2],
                        "away_total_throws": datatwo[3],
                        "away_att_miss_high_left": datatwo[4],
                        "away_blocked_scoring_att": datatwo[5],
                        "away_total_scoring_att": datatwo[6],
                        "away_att_sv_low_left": datatwo[7],
                        "away_total_tackle": datatwo[8],
                        "away_att_miss_high_right": datatwo[9],
                        "away_aerial_won": datatwo[10],
                        "away_att_miss_right": datatwo[11],
                        "away_att_sv_low_centre": datatwo[12],
                        "away_aerial_lost": datatwo[13],
                        "away_accurate_pass": datatwo[14],
                        "away_total_pass": datatwo[15],
                        "away_won_corners": datatwo[16],
                        "away_shot_off_target": datatwo[17],
                        "away_ontarget_scoring_att": datatwo[18],
                        "away_goals": datatwo[19],
                        "away_att_miss_left": datatwo[20],
                        "away_fk_foul_lost": datatwo[21],
                        "away_att_sv_low_right": datatwo[22],
                        "away_att_goal_low_centre": datatwo[22]
                    }
                }
                global_idpartidos = global_idpartidos +1
                print(json.dumps(matcjob))

                with open('final.json') as f:
                    data = json.load(f)

                data.update(matcjob)

                with open('final.json', 'w') as f:
                    json.dump(data, f)
        return global_idpartidos



    def ajustdata(datastats,idt,id):
        # hay algunos que no tiene
        ret = ["","","","","","","","","","","","","","","","","","","","","","","",""]
        try:
            ret[0] = datastats[id][idt]['aggregate_stats']['att_goal_low_left']
        except:
            ret[0] = ""
        try:
            ret[1] = datastats[id][idt]['aggregate_stats']['won_contest']
        except:
            ret[1] = ""
        try:
            ret[2] = datastats[id][idt]['aggregate_stats']['possession_percentage']
        except:
            ret[2] = ""
        try:
            ret[3] = datastats[id][idt]['aggregate_stats']['total_throws']
        except:
            ret[3] = ""
        try:
            ret[4] = datastats[id][idt]['aggregate_stats']['att_miss_high_left']
        except:
            ret[4] = ""
        try:
            ret[5] = datastats[id][idt]['aggregate_stats']['blocked_scoring_att']
        except:
            ret[5] = ""
        try:
            ret[6] = datastats[id][idt]['aggregate_stats']['total_scoring_att']
        except:
            ret[6] = ""
        try:
            ret[7] = datastats[id][idt]['aggregate_stats']['att_sv_low_left']
        except:
            ret[7] = ""
        try:
            ret[8] = datastats[id][idt]['aggregate_stats']['total_tackle']
        except:
            ret[8] = ""
        try:
            ret[9] = datastats[id][idt]['aggregate_stats']['att_miss_high_right']
        except:
            ret[9] = ""
        try:
            ret[10] = datastats[id][idt]['aggregate_stats']['aerial_won']
        except:
            ret[10] = ""
        try:
            ret[11] = datastats[id][idt]['aggregate_stats']['att_miss_right']
        except:
            ret[11] = ""
        try:
            ret[12] = datastats[id][idt]['aggregate_stats']['att_sv_low_centre']
        except:
            ret[12] = ""
        try:
            ret[13] = datastats[id][idt]['aggregate_stats']['aerial_lost']
        except:
            ret[13] = ""
        try:
            ret[14] = datastats[id][idt]['aggregate_stats']['accurate_pass']
        except:
            ret[14] = ""
        try:
            ret[15] = datastats[id][idt]['aggregate_stats']['total_pass']
        except:
            ret[15] = ""
        try:
            ret[16] = datastats[id][idt]['aggregate_stats']['won_corners']
        except:
            ret[16] = ""
        try:
            ret[17] = datastats[id][idt]['aggregate_stats']['shot_off_target']
        except:
            ret[17] = ""
        try:
            ret[18] = datastats[id][idt]['aggregate_stats']['ontarget_scoring_att']
        except:
            ret[18] = ""
        try:
            ret[19] = datastats[id][idt]['aggregate_stats']['goals']
        except:
            ret[19] = ""
        try:
            ret[20] = datastats[id][idt]['aggregate_stats']['att_miss_left']
        except:
            ret[20] = ""
        try:
            ret[21] = datastats[id][idt]['aggregate_stats']['fk_foul_lost']
        except:
            ret[21] = ""
        try:
            ret[22] = datastats[id][idt]['aggregate_stats']['att_sv_low_right']
        except:
            ret[22] = ""
        try:
            ret[23] = datastats[id][idt]['aggregate_stats']['att_goal_low_centre']
        except:
            ret[23] = ""
        return ret

    def result(data):
        home = data[0]
        away = data[-1]
        if home > away:
            return "H"
        elif home < away:
            return "A"
        else:
            return "D"




    def jsontocsv(directionjson):
        infile = open(directionjson, 'r')

        df = pd.read_json(infile)
        df.to_csv('../csvdatafile/season1/finalSeason.csv')
    main()
#execution
global_idpartidos =0
mainClass()