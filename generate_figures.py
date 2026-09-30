"""Generate exact diagrams and synthetic teaching data. No empirical TISE results."""
from pathlib import Path
import csv, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures'; DATA=ROOT/'data'
FIG.mkdir(exist_ok=True); DATA.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
BLUE='#0072B2'; ORANGE='#D55E00'; TEAL='#009E73'

def save(fig,name):
    fig.savefig(FIG/(name+'.svg'),bbox_inches='tight',facecolor='white')
    fig.savefig(FIG/(name+'.png'),dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)

def canvas(w=10,h=6):
    f,a=plt.subplots(figsize=(w,h)); a.set_xlim(0,10); a.set_ylim(0,7); a.axis('off'); return f,a

def box(a,x,y,w,h,label,color='#edf5fa'):
    a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06,rounding_size=0.12',facecolor=color,edgecolor='#36556b',linewidth=1.3))
    a.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=11)

def arrow(a,p,q,label='',dashed=False,rad=0):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=14,linewidth=1.3,color='#36556b',linestyle='--' if dashed else '-',connectionstyle=f'arc3,rad={rad}'))
    if label: a.text((p[0]+q[0])/2,(p[1]+q[1])/2+0.13,label,ha='center',va='bottom',fontsize=9,bbox={'facecolor':'white','edgecolor':'none','pad':2})

# 1: complementary representations
f,a=canvas()
box(a,3.5,5.8,3,0.8,'Pertanyaan dan klaim','#dceef7')
box(a,0.2,3.8,2.6,1,'Teks\nAlasan dan interpretasi')
box(a,3.7,3.8,2.6,1,'Diagram\nStruktur dan mekanisme')
box(a,7.2,3.8,2.6,1,'Plot\nPola dan variasi')
box(a,1.6,1.8,2.8,1,'Tabel\nNilai dan perbandingan')
box(a,5.6,1.8,2.8,1,'Gambar\nWujud dan kondisi')
for x in (1.5,5,8.5): arrow(a,(5,5.8),(x,4.8))
arrow(a,(1.5,3.8),(3,2.8));arrow(a,(8.5,3.8),(7,2.8))
arrow(a,(5,3.8),(3,2.8));arrow(a,(5,3.8),(7,2.8))
a.text(5,0.8,'Konsistensi antarbentuk memungkinkan pemeriksaan klaim',ha='center',fontsize=12,color=BLUE)
save(f,'01-representasi')

# 2: Triune intelligence without an AI authority hierarchy
f,a=canvas()
box(a,0.2,5.3,2.8,1.2,'Manusia\nTujuan dan tanggung jawab','#dceef7')
box(a,3.6,5.3,2.8,1.2,'Kolektif\nNorma dan legitimasi','#e1f3eb')
box(a,7,5.3,2.8,1.2,'AI\nAnalitik dan simulasi','#fff0da')
box(a,3.1,2.8,3.8,1.3,'Keputusan bersama\nBukti, persetujuan, batas')
box(a,3.1,0.4,3.8,1.2,'Ekosistem berorientasi misi\nHasil dan kapabilitas')
for x in (1.6,5,8.4): arrow(a,(x,5.3),(5,4.1))
arrow(a,(5,2.8),(5,1.6),'tindakan')
a.plot([6.9,8.2,8.2],[1,1,3.45],ls='--',color='#36556b',lw=1.3)
arrow(a,(8.2,3.45),(6.9,3.45),dashed=True)
a.text(8.45,2.2,'umpan balik',ha='left',va='center',fontsize=9)
save(f,'02-triune')

# 3: Q-Cycle with evidence returning to mission
f,a=canvas()
box(a,.5,4.7,3.8,1.5,'Q1 — Masalah dan misi\nKebutuhan, batas, target','#dceef7')
box(a,5.7,4.7,3.8,1.5,'Q2 — Analisis fungsional\nAliran, perilaku, ukuran','#eedfc9')
box(a,5.7,1,3.8,1.5,'Q3 — Sintesis arsitektur\nKomponen, peran, kendali','#fff3be')
box(a,.5,1,3.8,1.5,'Q4 — Konstruksi dan bukti\nBangun, uji, operasi','#f6f7f8')
arrow(a,(4.3,5.45),(5.7,5.45),'kebutuhan')
arrow(a,(7.6,4.7),(7.6,2.5),'fungsi')
arrow(a,(5.7,1.75),(4.3,1.75),'realisasi')
arrow(a,(2.4,2.5),(2.4,4.7),'bukti / revisi',True)
a.text(5,3.5,'Ketertelusuran\nQ1 ↔ Q2 ↔ Q3 ↔ Q4',ha='center',va='center',fontsize=12,color=BLUE)
save(f,'03-qcycle')

# 4: control and transformation; arrows have typed meanings
f,a=canvas(11,6)
box(a,.2,2.3,2.4,1.2,'SOURCE\nSumber daya')
box(a,3.6,2.3,2.8,1.2,'OPERATOR\nTransformasi inti')
box(a,7.4,2.3,2.4,1.2,'USER\nKeluaran dan nilai')
box(a,3.6,5.2,2.8,1,'REGULATOR\nAturan dan legitimasi','#e1f3eb')
box(a,3.6,.2,2.8,1.1,'Kendali PUDAL\nP–U–D–A–L','#fff0da')
arrow(a,(2.6,2.9),(3.6,2.9),'pasokan')
arrow(a,(6.4,2.9),(7.4,2.9),'layanan')
arrow(a,(5,5.2),(5,3.5),'batas',True)
arrow(a,(4.3,1.3),(4.3,2.3),'aksi disetujui')
arrow(a,(5.7,2.3),(5.7,1.3),'telemetri')
arrow(a,(8.6,2.3),(6.4,.8),'pengalaman pengguna',True)
save(f,'04-arsitektur')

# 5: claims and evidence are not interchangeable
f,a=canvas(11,6)
a.set_xlim(0,12)
box(a,.4,5.2,3.7,1.1,'Kebutuhan Q1\nTarget yang disepakati')
box(a,5.9,5.2,3.7,1.1,'Klaim penelitian\nPernyataan yang diuji')
box(a,.4,2.9,3.7,1.1,'Metode / arsitektur\nMekanisme yang diajukan')
box(a,5.9,2.9,3.7,1.1,'Protokol pengujian\nPembanding dan kondisi')
box(a,3.1,.3,3.8,1.2,'Bukti Q4\nData, plot, tabel, batas')
arrow(a,(4.1,5.75),(5.9,5.75),'memotivasi')
arrow(a,(2.25,5.2),(2.25,4),'diturunkan')
arrow(a,(7.75,5.2),(7.75,4),'dioperasionalkan')
arrow(a,(2.25,2.9),(4.3,1.5),'direalisasikan')
arrow(a,(7.75,2.9),(5.7,1.5),'menghasilkan')
a.plot([6.9,10.7,10.7],[.9,.9,5.75],ls='--',color='#36556b',lw=1.3)
arrow(a,(10.7,5.75),(9.6,5.75),dashed=True)
a.text(11,3.35,'mendukung / membatasi',rotation=90,ha='center',va='center',fontsize=9)
save(f,'05-bukti')

# 6: identical mean and SD, different patterns (constructed explicitly)
u=np.array([-3,-2,-1,-.5,.5,1,2,3.],float)
v=np.array([-1,-1,-1,-1,1,1,1,1.],float)
u=50+10*(u-u.mean())/u.std(ddof=1)
v=50+10*(v-v.mean())/v.std(ddof=1)
with (DATA/'distribusi-sintetis.csv').open('w') as fp:
    writer=csv.writer(fp);writer.writerow(['kelompok','observasi','nilai'])
    for label,xs in [('A',u),('B',v)]:
        for i,x in enumerate(xs):writer.writerow([label,i+1,f'{x:.10f}'])
f,axs=plt.subplots(1,2,figsize=(10,4.2),sharey=True,layout='constrained')
axs[0].bar([0,1],[u.mean(),v.mean()],yerr=[u.std(ddof=1),v.std(ddof=1)],color=[BLUE,ORANGE],alpha=.75,capsize=7,width=.55)
axs[0].set_title('A. Ringkasan identik: rerata ± SD')
for i,(xs,c) in enumerate([(u,BLUE),(v,ORANGE)]):
    axs[1].scatter(i+np.linspace(-.12,.12,len(xs)),xs,c=c,s=55,zorder=3)
    axs[1].plot([i-.24,i+.24],[xs.mean()]*2,color='black',lw=2)
axs[1].set_title('B. Titik individual: pola berbeda')
for a in axs:a.set_xticks([0,1],['Kelompok A','Kelompok B']);a.set_ylim(0,75);a.grid(axis='y',alpha=.2)
axs[0].set_ylabel('Nilai ilustratif (unit arbitrer)')
save(f,'06-distribusi')

# 7: exact paired data, no inferential or population claim
before=np.array([12,11,14,10,13,9,15,12,11,13,10,14.])
after=np.array([9,9,11,9,10,10,12,10,8,11,9,11.])
delta=after-before
with (DATA/'berpasangan-sintetis.csv').open('w') as fp:
    writer=csv.writer(fp);writer.writerow(['kasus','sebelum_menit','sesudah_menit','selisih_menit'])
    for i,(b,c) in enumerate(zip(before,after)):writer.writerow([i+1,b,c,c-b])
f,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
for b,c in zip(before,after):axs[0].plot([0,1],[b,c],'-o',color=ORANGE if c>b else BLUE,alpha=.7)
axs[0].set_xticks([0,1],['Sebelum','Sesudah']);axs[0].set_ylabel('Waktu layanan (menit)');axs[0].set_title('A. Kasus yang sama dihubungkan')
axs[0].set_ylim(0,17)
axs[1].scatter(np.arange(1,13),delta,c=[ORANGE if d>0 else BLUE for d in delta]);axs[1].axhline(0,color='gray',ls='--')
axs[1].axhline(delta.mean(),color=TEAL,label=f'Rerata selisih = {delta.mean():.2f} menit')
axs[1].set_xlabel('Kasus sintetis');axs[1].set_ylabel('Sesudah − sebelum (menit)');axs[1].set_title('B. Variasi perubahan individual');axs[1].legend(fontsize=9)
for a in axs:a.grid(axis='y',alpha=.2)
save(f,'07-berpasangan')

# 8: entirely specified synthetic dynamics with a recovery criterion
t=np.arange(0,61)
base=2+14*np.exp(-np.maximum(t-20,0)/18)*(t>=20)
adapt=2+14*np.exp(-np.maximum(t-20,0)/6)*(t>=20)
with (DATA/'pemulihan-sintetis.csv').open('w') as fp:
    writer=csv.writer(fp);writer.writerow(['waktu_menit','baseline_galat_persen','adaptif_galat_persen'])
    for ts,b,c in zip(t,base,adapt):writer.writerow([ts,f'{b:.10f}',f'{c:.10f}'])
f,a=plt.subplots(figsize=(10,4.3),layout='constrained')
a.plot(t,base,color=BLUE,ls='--',label='Baseline ilustratif: τ = 18 menit')
a.plot(t,adapt,color=ORANGE,label='Adaptif ilustratif: τ = 6 menit')
a.axvline(20,color='gray',ls=':',label='Gangguan: menit ke-20')
a.axhline(5,color=TEAL,ls='-.',label='Batas pemulihan ilustratif: ≤5%')
a.set_xlabel('Waktu (menit)');a.set_ylabel('Galat keluaran (%)');a.set_ylim(0,18);a.legend(fontsize=9);a.grid(alpha=.2)
a.set_title('Respons sintetis: parameter pemulihan ditentukan pembuat contoh')
save(f,'08-pemulihan')

stats={'distribution':{'n':8,'mean_A':float(u.mean()),'sd_A':float(u.std(ddof=1)),'mean_B':float(v.mean()),'sd_B':float(v.std(ddof=1))},'paired':{'n':12,'before_mean':float(before.mean()),'after_mean':float(after.mean()),'delta_mean':float(delta.mean()),'delta_sd':float(delta.std(ddof=1)),'improved':int((delta<0).sum()),'worsened':int((delta>0).sum())},'recovery':{'baseline_first_recovered_minute':int(t[(t>=20)&(base<=5)][0]),'adaptive_first_recovered_minute':int(t[(t>=20)&(adapt<=5)][0])}}
(DATA/'ringkasan.json').write_text(json.dumps(stats,indent=2))
print(json.dumps(stats,indent=2))
