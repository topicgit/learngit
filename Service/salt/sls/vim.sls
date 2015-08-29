# 将vim配置文件vimrc推送到从机
/root/.vimrc:
 file.managed:
  - source: salt://base_sys/vimrc
  - mode: 644
  - user: root
  - group: root
