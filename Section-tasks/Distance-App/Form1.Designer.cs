namespace Distance_App
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Calcbtn = new System.Windows.Forms.Button();
            this.Hrs_trvld = new System.Windows.Forms.TextBox();
            this.Spdtxt = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.resultlst = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // Calcbtn
            // 
            this.Calcbtn.Location = new System.Drawing.Point(354, 334);
            this.Calcbtn.Name = "Calcbtn";
            this.Calcbtn.Size = new System.Drawing.Size(75, 23);
            this.Calcbtn.TabIndex = 0;
            this.Calcbtn.Text = "Calculate";
            this.Calcbtn.UseVisualStyleBackColor = true;
            this.Calcbtn.Click += new System.EventHandler(this.Calcbtn_Click);
            // 
            // Hrs_trvld
            // 
            this.Hrs_trvld.Location = new System.Drawing.Point(384, 120);
            this.Hrs_trvld.Name = "Hrs_trvld";
            this.Hrs_trvld.Size = new System.Drawing.Size(100, 23);
            this.Hrs_trvld.TabIndex = 1;
            // 
            // Spdtxt
            // 
            this.Spdtxt.Location = new System.Drawing.Point(384, 62);
            this.Spdtxt.Name = "Spdtxt";
            this.Spdtxt.Size = new System.Drawing.Size(100, 23);
            this.Spdtxt.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(301, 65);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(39, 15);
            this.label1.TabIndex = 3;
            this.label1.Text = "Speed";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(275, 123);
            this.label2.Name = "label2";
            this.label2.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.label2.Size = new System.Drawing.Size(85, 15);
            this.label2.TabIndex = 4;
            this.label2.Text = "Hours Traveled";
            // 
            // resultlst
            // 
            this.resultlst.FormattingEnabled = true;
            this.resultlst.ItemHeight = 15;
            this.resultlst.Location = new System.Drawing.Point(236, 159);
            this.resultlst.Name = "resultlst";
            this.resultlst.Size = new System.Drawing.Size(327, 169);
            this.resultlst.TabIndex = 5;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.resultlst);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Spdtxt);
            this.Controls.Add(this.Hrs_trvld);
            this.Controls.Add(this.Calcbtn);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button Calcbtn;
        private TextBox Hrs_trvld;
        private TextBox Spdtxt;
        private Label label1;
        private Label label2;
        private ListBox resultlst;
    }
}