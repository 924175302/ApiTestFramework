import pymysql


# 创建工具类
class DButil():
    __conn = None
    __cursor = None

    # 创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database=""
            )
        return cls.__conn

    # 获取游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None

    # 执行sql
    @classmethod
    def exec_sql(cls, sql):
        try:
            # 获取游标对象
            cursor = cls.__get_cursor()
            # 调用游标对象的execute方法，执行sql
            cursor.execute(sql)
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回受影响的行数
                return cursor.rowcount
        except Exception as e:
            # 事务回滚
            cls.__conn.rollback()
            print(e)
        finally:
            # 关闭游标
            cls.__close_cursor()
            # 关闭连接
            cls.__close_conn()

    @classmethod
    def delete(cls, db_name, sql):
        try:
            cursor = cls.__get_cursor()
            cursor.execute(sql)
        except Exception as e:
            cls.__conn.rollback()
        finally:
            cls.__close_cursor()
            cls.__get_conn()
