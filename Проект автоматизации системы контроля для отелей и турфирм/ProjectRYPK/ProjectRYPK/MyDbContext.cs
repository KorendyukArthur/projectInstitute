﻿using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectRYPK
{
    public class MyDbContext : DbContext
    {
        public MyDbContext() : base("DbConnectionString")
        {
        }
    }
}
